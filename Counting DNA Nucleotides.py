string=open("rosalind_dna.txt").readlines()
sequence=string[0]
nts=list(sequence)
database={}
for i in range(len(nts)): 
    if nts[i] in database: 
        database[nts[i]]+=1
    else: database[nts[i]]=1
for key, value in database.items(): 
    print (key, value)