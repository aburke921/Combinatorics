# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:52:42 2021

@author: emmiller
"""
import math


def partial_permutation(n, k):
    factor = math.factorial(n)
    nminkkfact = math.factorial(n - k)
    kfact = math.factorial(k)

    denominator = kfact * nminkkfact
    return (factor / nminkkfact)


print(partial_permutation(21, 7) % 1000000)

 