#!/usr/bin/env python

from __future__ import division
import argparse
import json
from json.encoder import JSONEncoder
import math
from os.path import dirname, realpath
from pyspark import SparkContext, SparkConf
import time
import os

VIRTUAL_COUNT = 10
PRIOR_CORRELATION = 0.0
THRESHOLD = 0.5


##### Metric Functions ############################################################################
def correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy):
    # http://en.wikipedia.org/wiki/Correlation_and_dependence
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt(n * sum_xx - sum_x * sum_x) * math.sqrt(n * sum_yy - sum_y * sum_y)
    if denominator == 0:
        return 0.0
    return numerator / denominator

def regularized_correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy, virtual_count, prior_correlation):
    unregularized_correlation_value = correlation(n, sum_x, sum_y, sum_xx, sum_yy, sum_xy)
    weight = n / (n + virtual_count)
    return weight * unregularized_correlation_value + (1 - weight) * prior_correlation

def cosine_similarity(sum_xx, sum_yy, sum_xy):
    # http://en.wikipedia.org/wiki/Cosine_similarity
    numerator = sum_xy
    denominator = (math.sqrt(sum_xx) * math.sqrt(sum_yy))
    if denominator == 0:
        return 0.0
    return numerator / denominator

def jaccard_similarity(n_common, n1, n2):
    # http://en.wikipedia.org/wiki/Jaccard_index
    numerator = n_common
    denominator = n1 + n2 - n_common
    if denominator == 0:
        return 0.0
    return numerator / denominator
#####################################################################################################

##### util ##########################################################################################
def combinations(iterable, r):
    # http://docs.python.org/2/library/itertools.html#itertools.combinations
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(list(range(r))):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
#####################################################################################################


def parse_args():
    parser = argparse.ArgumentParser(description='MapReduce similarities')
    parser.add_argument('-d', help='path to data directory', default='./../data/recommendations/small/')
    parser.add_argument('-n', help='number of data slices', default=128)
    parser.add_argument('-o', help='path to output JSON', default="output")
    return parser.parse_args()

# Feel free to create more mappers and reducers.
def mapper0(record):
    r = record.split('::')
    if len(r) == 2:
        yield (r[0], [r])
    else:
        yield (r[1], [r])

def reducer(a, b):
    # TODO
    return a + b

def mapper1(record):
    # Hint: 
    # INPUT:
    #   record: (key, values)
    #     where -
    #       key: movie_id
    #       values: a list of values in the line
    # OUTPUT:
    #   [(key, value), (key, value), ...]
    #     where -
    #       key: movie_title
    #       value: [(user_id, rating)]
    #
    # TODO
    reviews = []
    for review in record[1][1:]:
        reviews.append([review[0], int(review[2])])
    yield (record[1][0][1], reviews)

def mapper2(record):
    n = len(record[1][1:])
    for review in record[1][1:]:
        yield(review[0], [(record[1][0][1] + f' {n}', float(review[2]))])

def mapper3(record):
    for r1, r2 in combinations(record[1], 2):
        name1 = r1[0]
        name2 = r2[0]
        rating1 = r1[1]
        rating2 = r2[1]
        if name1 < name2:
            yield((name1, name2), [(rating1, rating2)])
        else:
            yield((name2, name1), [(rating1, rating2)])

def mapper4(record):
    n = x = xx = y = yy = xy = 0
    for r1, r2 in record[1]:
        x += r1
        y += r2
        xx += r1 * r1
        yy += r2 * r2
        xy += r1 * r2
        n += 1
    s1 = record[0][0].rfind(' ')
    s2 = record[0][1].rfind(' ')
    n1 = float(record[0][0][s1: ].strip())
    n2 = float(record[0][1][s2: ].strip())
    cor = correlation(n, x, y, xx, yy, xy)
    reg_cor = regularized_correlation(n, x, y, xx, yy, xy, VIRTUAL_COUNT, PRIOR_CORRELATION)
    cos = cosine_similarity(xx, yy, xy)
    jac = jaccard_similarity(n, n1, n2)
    if reg_cor >= THRESHOLD:
        yield(record[0][0][:s1], [[record[0][1][:s2], cor, reg_cor, cos, jac, n, n1, n2]])

def mapper5(record):
    for r in record[1]:
        yield((record[0], r[0]), r[1:])

def main():
    args = parse_args()
    conf = SparkConf().set('spark.driver.host','127.0.0.1')
    sc = SparkContext(conf = conf)

    with open(args.d + '/movies.dat', 'r') as mlines:
        data = [line.rstrip() for line in mlines]
    with open(args.d + '/ratings.dat', 'r') as rlines:
        data += [line.rstrip() for line in rlines]
    
    # Implement your mapper and reducer function according to the following query.
    # stage1_result represents the data after it has been processed at the second
    # step of map reduce, which is after mapper1.\
    stage1_result = sc.parallelize(data, args.n).flatMap(mapper0).reduceByKey(reducer) \
                                                .flatMap(mapper1).reduceByKey(reducer)
    if not os.path.exists(args.o):
        os.makedirs(args.o)

    # Store the stage1_output
    with open(args.o  + '/netflix_stage1_output.json', 'w') as outfile:
        json.dump(stage1_result.collect(), outfile, separators=(',', ':'))

    # TODO: continue to build the pipeline
    # Pay attention to the required format of stage2_result
    stage2_result = sc.parallelize(data, args.n).flatMap(mapper0).reduceByKey(reducer).flatMap(mapper2).reduceByKey(reducer) \
                                                .flatMap(mapper3).reduceByKey(reducer).flatMap(mapper4).reduceByKey(reducer)
    # print(stage2_result[:20])

    # Store the stage2_output
    with open(args.o  + '/netflix_stage2_output.json', 'w') as outfile:
        json.dump(stage2_result.collect(), outfile, separators=(',', ':'))

    # TODO: continue to build the pipeline
    final_result = stage2_result.flatMap(mapper5).reduceByKey(reducer).collect()

    with open(args.o + '/netflix_final_output.json', 'w') as outfile:
        json.dump(final_result, outfile, separators=(',', ':'))

    sc.stop()



if __name__ == '__main__':
    main()
