string=open("rosalind_revc.txt").readlines()
sequence=string[0]
#print (sequence)
original=list(sequence)
original.pop() #removes new line character from end of list
#print(original)
flipped=list(reversed(original))
#print (flipped)
compliment=list()
for i in range(len(original)): 
    if flipped[i]=='A': 
        compliment.insert(i, 'T')
    elif flipped[i]=='C': 
        compliment.insert(i, 'G')
    elif flipped[i]=='G': 
        compliment.insert(i, 'C')
    elif flipped[i]=='T': 
        compliment.insert(i, 'A')
    else: compliment.insert(i, 'X') #debug 
printcompliment=''.join(compliment)
print(printcompliment)