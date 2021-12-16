import math

from math import factorial
import sys
sys.float_info.max
def  bi_sum(n, k):
   # nplus = n+1
   c = 0
   for i in range(k, n+1):
         c+=(factorial(n))/(factorial(i)*factorial(n-i))
   print(c%1000000)

