##data import and manipulation##
with open('rosalind_lcsm.txt') as f: #workaround for weird import issue
    file=f.read()
rawdata=file.split('>') #split data into strings based on FASTA title character
del rawdata[0] #remove empty string from beginning of list
stringlist=[] #list that will store strings
for string in rawdata: #for each string in list of all strings
    b=string.split('\n',1) #split at first newline to separate title from string
    c=b[1].replace('\n','') #remove newline characters
    stringlist.append(c) #store strings in string list

##creating list of all possible substrings##
combos=[] #list to store lists of all possible substrings of each DNA string
for a in range(len(stringlist)): #for each DNA string
    combos2=[] #blank list to store substrings for each DNA string 
    for idx in range(len(stringlist[a])+1): 
        combos2.extend([stringlist[a][j:j+idx] for j in range(len(stringlist[a])-idx+1)]) #creates list of all substrings for each DNA string
    combos.append(combos2) #combines above lists into list of lists of substrings

##looking for shared motif##
#k=indexed length of list of all DNA string substring lists
#m as iterated: each substring for each DNA string
#n=repeat of k
#combos[k] as iterated: each list of DNA substrings
commonstring='' #blank string to store longest common substring
for k in combos: #iterate through list of DNA strings
    for m in k: #iterate through each DNA string- m is each element in DNA string
        found=False
        for n in combos:
            if m in n: #if substring m is found in n(list of all possible substrings)
                found=True
            else: 
                break #end the foor loop for computational efficiency
        if found and len(m)>len(commonstring): #if the substring is found in all DNA strings and is the longest substring found
            commonstring=m #store it as the common motif
print(commonstring) #and print it
