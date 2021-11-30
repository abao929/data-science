from numpy.core.numeric import cross
from util import all_variable_names_in_df
import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel, chi2_contingency


def one_sample_ttest(values, population_mean):
    """
    Input:
    - values: a 1-d array (can be a numpy array, or a Python array) representing the
                samples
    - population_mean: a float, that is the mean of the population (and not of
                        the samples that we're seeing in values)
    Output:
    - tstats: a float, describing the t statistics
    - p-value: a float, describing the two-tailed p-value
    """
    # TODO: Use scipy's ttest_1samp
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html)
    # to get the t-statistic and the p-value.
    tstats, pvalue = ttest_1samp(values, population_mean)

    ## TODO: You can uncomment to print out the test statistics and pvalue to 
    ## determine your answer to the questions
    print("Test statistics: ", tstats)
    print("p-value: ", pvalue)
    print("p-value < 0.05", pvalue < 0.05)
    
    # and then we'll return tstats and pvalue
    return tstats, pvalue


def two_sample_ttest(values_a, values_b):
    """
    Input:
        - values_a: a 1-d array of numbers that is one set of samples
        - values_b: a 1-d array of numbers that is the other set of samples
    Output:
        - tstats: a float, describing the t statistics
        - p-value: a float, describing the two-tailed p-value
    """
    # TODO: Use scipy's ttest_ind
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
    # to get the t-statistic and the p-value
    # Note: Be sure to make the function call in a way such that the code will disregard
    # null (nan) values. Additionally, you can assume equal variance.
    # Note: This is unpaired two sample t-test
    tstats, pvalue = ttest_ind(values_a, values_b)

    ## TODO: You can uncomment to print out the test statistics and pvalue to 
    ## determine your answer to the questions
    print("Test statistics: ", tstats)
    print("p-value: ", pvalue)
    print("p-value < 0.05", pvalue < 0.05)

    # and then we'll return tstats and pvalue
    return tstats, pvalue


def paired_ttest(values_a, values_b):
    """
    Input:
        - values_a: a 1-d array of numbers that is one set of samples
        - values_b: a 1-d array of numbers that is the other set of samples
                * Note on input: len(values_a) and len(values_b) have to be the 
                same, and samples of values_a and values_b are treated as pairs
                - i.e. (a_i, b_i) (for all i < len(values_a)) are treated as pairs.
    Output:
        - tstats: a float, describing the t-statistics
        - p-value: a float, describing the two-tailed p-value
    """
    # TODO: Use scipy's ttest_rel
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html)
    # to get the test tatistic and the p-value
    # Note: Be sure to make the function call in a way such that the code will disregard
    # null (nan) values.
    tstats, pvalue = ttest_rel(values_a, values_b)

    ## TODO: You can uncomment to print out the test statistics and pvalue to 
    ## determine your answer to the questions
    print("Test statistics: ", tstats)
    print("p-value: ", pvalue)
    print("p-value < 0.05", pvalue < 0.05)

    # and then we'll return tstats and pvalue
    return tstats, pvalue


def chisquared_independence_test(df, column_a_name, column_b_name):
    """
    Input:
        - df: a Pandas DataFrame
        - column_a_name: str, a name of a feature in the table df
        - column_b_name: str, a name of another feature in the table df
    Output:
        - tstats: a float, describing the test statistics
        - p-value: describing the p-value of the test
    """
    ## Stencil: Error check input - do not modify this part
    assert all_variable_names_in_df([column_a_name, column_b_name], df)

    # TODO: Create a cross table between the two columns a and b
    # Hint: If you are unsure how to do this, refer to the stats lab!
    cross_table = pd.crosstab(df[column_a_name], df[column_b_name])

    # TODO: Use scipy's chi2_contingency
    # (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
    # to get the test statistic and the p-value
    tstats, pvalue, d, e = chi2_contingency(cross_table)

    ## TODO: You can uncomment to print out the test statistics and pvalue to 
    ## determine your answer to the questions
    print("Test statistics: ", tstats)
    print("p-value: ", pvalue)
    print("p-value < 0.05", pvalue < 0.05)

    # and then we'll return tstats and pvalue
    return tstats, pvalue
