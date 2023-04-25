# -*- coding: utf-8 -*-
"""
Student: Roye Fanka
Year: 2020
"""
#=============================================================================
#%%

# Problem 1: Curve Fitting

import numpy as np

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    return [np.polyfit(x, y, z) for z in degs]

#=============================================================================
#%%

# Problem 2: R^2

import numpy as np

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    y, estimated = np.array(y), np.array(estimated)
    SEE = ((estimated - y)**2).sum()
    mMean = y.sum()/float(len(y))
    MV = ((mMean - y)**2).sum()
    return 1 - SEE/MV

#%%


