##importing and formatting Rosalind dataset**
string=open('rosalind_lgis.txt').readlines() #import Rosalind file
permutation=string[1].split() #store permutation in list
permutation=list(map(int, permutation)) #turn numeric strings into integers

def LIS(permutation): #function to find longest increasing subsequence
    lis_len = [1] * len(permutation) #store length of permutation in list
    for i in range(len(permutation)): #for each number in permutation
        for j in range(i+1, len(permutation)): #starting from each number in permutation
            if permutation[i] < permutation[j]: #if the previous number is less than the next number
                lis_len[j] = max(lis_len[j], lis_len[i] + 1) #add number to list
    rv = [] #create list to store final numbers
    curr_len = max(lis_len) 
    for i in range(len(permutation) - 1, -1, -1): #for each permutation, working backwards
        if curr_len == lis_len[i]: #if previous permutation is shorter than current 
            rv.append(permutation[i]) #overwrite LIS list
            curr_len -= 1
    return rv[::-1]

def LDS(permutation): #function to find longest decreasing subsequence
    lds_len = [1] * len(permutation) #store length of permutation in list
    for i in range(len(permutation)): #for each number in permutation
        for j in range(i+1, len(permutation)): #starting from each number in permutation
            if permutation[i] > permutation[j]: #if the previous number is less than the next number
                lds_len[j] = max(lds_len[j], lds_len[i] + 1) #add number to list
    rv = [] #create list to store final numbers
    curr_len = max(lds_len)
    for i in range(len(permutation) - 1, -1, -1): #for each permutation, working backwards
        if curr_len == lds_len[i]: #if previous permutation is shorter than current 
            rv.append(permutation[i]) #overwrite LIS list
            curr_len -= 1
    return rv[::-1]


increasinglist=LIS(permutation)
decreasinglist=LDS(permutation)

increasinglist=list(map(str, increasinglist)) #turn integers back into numeric strings
increasingfinallist=' '.join(increasinglist) #turn into string with spaces between numbers
print(increasingfinallist)
decreasinglist=list(map(str, decreasinglist)) #turn integers back into numeric strings
decreasingfinallist=' '.join(decreasinglist) #turn into string with spaces between numbers
print(decreasingfinallist)