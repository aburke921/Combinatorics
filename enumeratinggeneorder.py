# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:42:58 2021

@author: emmiller
"""
from itertools import permutations

def geneorder(n):

    nums = []
    for i in range(1, n+1):
        nums.append(i)
    perm = permutations(nums, len(nums))
    for i in list(perm):
        print(i)

geneorder(3)
