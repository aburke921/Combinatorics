string=open("rosalind_rna.txt").readlines()
sequence=string[0]
#print (sequence)
RNA=list(sequence)
DNA=list()
for i in range(len(RNA)): 
    if RNA[i]=='T': 
        DNA.insert(i, 'U')
    else: DNA.insert(i, RNA[i])
DNA.pop
printDNA=''.join(DNA)
print(printDNA)