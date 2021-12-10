from math import factorial 
def  bi_sum(n, k):
   # nplus = n+1
    for i in range(k, n):
        sol =  (1 + factorial(n))%1000000
        so12 = factorial(k)*factorial(n-k)
        print(sol)
bi_sum(1913, 1099)
