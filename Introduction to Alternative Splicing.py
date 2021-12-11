from math import factorial
import sys
sys.float_info.max
def  bi_sum(n, k):
   # nplus = n+1
    for i in range(k, n):
        sol =  (1 + factorial(n))
        so12 = factorial(k)*factorial(n-k)
    return(sol//so12)%1000000
print(bi_sum(1913, 1099))
