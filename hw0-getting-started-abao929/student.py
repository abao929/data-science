##### IMPORTS #####
# This is an example of how you import packages in Python
import sys
# this is an example of how you import a submodule from a package in Python. While running the program,
# if you run into a "ModuleNotFoundError: No module named PySpark", it means that you either are not running
# this code using your virtual environment, or your virtual environment set up did not happen properly. Come
# to TA hours or post on Piazza to get support!
from pyspark import SparkContext
from operator import add
# TODO: Look up how to import the packages: os, datetime, numpy (naming it as np), 
#                                           matplotlib.pyplot (naming it as plt), pandas (naming it as pd)
# Hint: Try queries like "How to import _____ python" on Google
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
###### VARIABLE DEFINITIONS #####

add_one_to_x = lambda x: x + 1 # TODO: Fix this function
increment_each_by_one = lambda x: list(map(add_one_to_x, x)) # TODO: None is only used as a placeholder. Please redefine this function to perform correctly
def add_odd_elements(input_list: list):
    """
    input: list of integers. For example, [1, 2, 3, 4, 5]
    output: an integer that is the sum of all the numbers in odd positions (0 indexed)
    example:
    - add_odd_elements([1, 2, 3, 4, 5]) == 2 + 4 == 6
    - add_odd_elements([]) == 0
    - add_odd_elements([1]) == 0
    - add_odd_elements([1, 2, 3, 4, 5, 6]) == 2 + 4 + 6 == 12
    """
    # TODO: Implement this function
    return sum(input_list[1::2])


def filter_even_numbers(input_list: list):
    """
    input: list of integers. For example, [2, 3, 4, 5, 6, 10, 11]
    output: a list of integers that are from the original list of integers, *BUT* only even
            numbers - and in its order
    example:
    - filter_even_numbers([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    - filter_even_numbers([]) == []
    - filter_even_numbers([1, 3, 5, 7]) == []
    """
    # TODO: Implement this function
    return list(filter(lambda x: x%2 == 0, input_list))


def function_to_debug(input: str):
    """
    input: a string, e.g. "It's Always Sunny In Philadelphia YEEHAW"
    output: a string without all the vowels (a, e, i, o, u), e.g. "t's lwys Snny n Phldph YHW"
    """
    # TODO: Debug this function to make sure that it works as you expect
    input_string = input.replace("a", "")
    input_string = input_string.replace("e", "")
    input_string = input_string.replace("i", "")
    input_string = input_string.replace("o", "")
    input_string = input_string.replace("u", "")
    input_string = input_string.replace("A", "")
    input_string = input_string.replace("E", "")
    input_string = input_string.replace("I", "")
    input_string = input_string.replace("O", "")
    input_string = input_string.replace("U", "")
    return input_string


############### DO NOT MODIFY THE CODE BELOW ###############
def plot_silly_graph():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.axis([0, 6, 0, 20])
    plt.title("To The Moon!")
    plt.savefig("tothemoon.png")
    plt.show()
    


def check_mapreduce_installation_correct():
    print("Checking if the setup for MapReduce is done properly or not")
    # input sentence, then turn it into a list of words
    sentence = "MapReduce Map Reduce Mapper Reducer MapReduce"
    data = sentence.split()
    # create a new instance of Spark pipeline
    sc = SparkContext()
    # Turning off info messages being displayed in spark control
    sc.setLogLevel("OFF")
    word_count = sc.parallelize(data, 128) \
                   .map(lambda word: (word, 1)) \
                   .reduceByKey(add) \
                   .sortByKey(True) \
                   .collect()
    sc.stop()


if __name__ == "__main__":
    # running mapreduce to check if the installation is properly
    check_mapreduce_installation_correct()
    # This part is to test if you have imported everything correctly & set up the virtual environment, Python and java correctly
    assert os.path.exists("student.py")
    print("The datetime today is: ", datetime.datetime.today())
    my_np_array = np.array([1, 2, 3 , 4, 5])
    my_pandas_table = pd.DataFrame([[1, "a"], [2, "b"], [3, "c"], [4, "d"]], columns=["number", "characters"])
    # TODO: Print out my_np_array and my_pandas_table to see what they look like!
    
    # and then plot the graphs - press x to close the graph when you're finished
    plot_silly_graph()
    # This part is to test your functions above
    assert add_one_to_x(1) == 2, "add_one_to_x function is incorrect - please fix"
    assert increment_each_by_one([11, 12, 2000, 10, 14, 1998]) == [12, 13, 2001, 11, 15, 1999], "increment_each_by_one function is incorrect - please fix"
    assert add_odd_elements([1, 2, 3, 4, 5]) == 6
    assert add_odd_elements([]) == 0
    assert add_odd_elements([1]) == 0
    assert add_odd_elements([1, 2, 3, 4, 5, 6]) == 12
    assert filter_even_numbers([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert filter_even_numbers([1, 3, 5, 7]) == []
    assert function_to_debug("It's Always Sunny In Philadephia YEEHAW") == "t's lwys Snny n Phldph YHW"
    assert function_to_debug("") == ""
    assert function_to_debug("DRGNVLL") == "DRGNVLL"
