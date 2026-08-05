"""
Module: sensorkit/stats.py
Contributor: Nana Amoabeng Brown
Student ID: 95072029
Date: 05/08/26
Role: Simple summary statistics for a list of numeric readings.

Complete the TODOs below.
"""


def mean(values):
    if values:
        return (sum(values)/len(values))
    else:
        raise ValueError("mean() needs values")


def minimum(values):
    return min(values)


def maximum(values):
    return max(values)


def spread(values):
    return (maximum(values) - minimum(values))
