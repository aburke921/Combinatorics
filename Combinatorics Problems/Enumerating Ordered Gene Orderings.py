    
# enumerating oriented gene orderings
# combinatorics #7
    

import itertools
    
n = 3
permutation = []
x = 0
for i in itertools.permutations(list(range(1, n+1))):
    for j in itertools.product([-1,1],repeat = len(list(range(1, n+1)))):
        perms = [a*sign for a, sign in zip(i, j)]
        permutation.append(perms)
        x += 1
print(x)

for i in range(len(permutation)):
    print(*permutation[i], sep = ' ')
    
    
