# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:52:42 2021

@author: emmiller
"""
import math

def partial_permutation(n, k):

    return calculatePartialFactorial(n-k, n)

def calculatePartialFactorial(start, stop):

    factorial = 1
    for val in range(start + 1, stop + 1):
        # print(val)
        factorial = factorial * val

    return factorial

'''
    EXAMPLE:
    
                  21!         21 * 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    p(21, 7) =  -------   =   ----------------------------------------------------------------------------------------------
               (21 - 7)!                                         14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
                                                       
              
    p(21, 7) =  21 * 20 * 19 * 18 * 17 * 16 * 15 
'''




# def partial_permutation(n, k):
#     factor = math.factorial(n)
#     nminkkfact = math.factorial(n - k)
#     kfact = math.factorial(k)
#
#     denominator = kfact * nminkkfact
#     return (factor / nminkkfact)


print(partial_permutation(96, 9) % 1000000)


 