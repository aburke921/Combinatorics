import math

file = open('rosalind_sset.txt', 'r')
n = int(file.read())

numSubsets = int(math.pow(2,n))

print(numSubsets % 1000000)