string=open('rosalind_rear.txt').readlines() #import Rosalind file
for i in range(len(string)): #for loop to manipulate import into individual lists of integers for each permutation
    string[i]=string[i].split()
    string[i]=list(map(int, string[i]))
    print(string[i])

#Park's Exact Greedy Algorithm
def reverse(sequence, start, end): #function to perform reversal between start and end indices
    pre=sequence[:start] #sequence up to start index
    revsec=sequence[start:end][::-1] #sequence in between start and end read in reverse
    post=sequence[end:] #sequence up to end index
    return pre+revsec+post #combining parts

def getbreakpoints(sequence, target): #function to find breakpoints between 2 sequences
    breakpts=[]
    for i in range(len(sequence)-1): #for each value in original sequence
        current=sequence[i] #store current value
        adjacent=sequence[i+1] #store next value
        if abs(target.index(current)-target.index(adjacent)) != 1: #if original sequence values aren't adjacent in target sequence
            breakpts.append(i+1) #add next value breakpoints list
    return breakpts #returns a list of all breakpoints between sequences

def minimumreversals(sequences, target): 
    revs=[] #create list to store reversals
    for seq in sequences: 
        bkpts=getbreakpoints(seq, target) #use getbreapoints function
        for j in range(len(bkpts)-1): #iterate whole sequence over the number of breakpoints
            for k in range(j+1, len(bkpts)): #iterate from above to end of sequence as subsequences
                revs.append(reverse(seq, bkpts[j], bkpts[k])) #add reversals to list
    minbkpts=len(target) #minimum number of breakpoints is number of reversals performed
    minrev=[] #create list to store minimum number of reversals
    for rev in revs: #for each reversal
        numbkpts=len(getbreakpoints(rev, target)) #count number of breakpoints using function
        if numbkpts<minbkpts: #if the current number of breakpoints is less than previous min
            minbkpts=numbkpts #overwrite minimum number of breakpoints
            minrev=[rev] #overwrite minimum number of reversals
        elif numbkpts==minbkpts: #if the same number of breakpoints as previous min
            minrev.append(rev) #overwrite minimum number of reversals without changing minimum breakpoints
    return minrev #returns minimum number of required reversals to get to target from original sequence

def revdistance(sequence, target): #function that combines above functions to find reversal distance
    sequence=['-']+sequence+['+'] #formatting to allow combining of returns from other functions
    target=['-']+target+['+']
    revs=0 #counter to keep track of reversals used
    current=[sequence] #stores formatted sequence phrase in list to work with functions
    while target not in current: #until the two permutations match eachother:
        current=minimumreversals(current, target) #continue making reversals
        revs+=1 #adds one to counter for each reversal 
    return revs

#implementtation of functions to solve provided dataset
print(revdistance(string[0], string[1]), revdistance(string[3], string[4]), revdistance(string[6], string[7]), revdistance(string[9], string[10]), revdistance(string[12], string[13]))
