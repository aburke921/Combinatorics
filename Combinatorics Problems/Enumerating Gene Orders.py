import math                                         
import itertools    

# enumerating gene orders
# combinatorics #5


 #input is n                               
n = 6
print(math.factorial(n))                            
perms = itertools.permutations(list(range(1, n + 1)))

for i, j in enumerate(list(perms)):                  
    permutation = ''                                
    for item in j:                                  
        permutation += str(item) + ' '              
    print(permutation)
