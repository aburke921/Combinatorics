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

##sorting and subdividing strings##
srtinglist=sorted(stringlist, key=len) #sort list of strings from shortest to longest
shortest=stringlist[0] #separate the shortest string to check against others
complete=stringlist[1:] #store the rest of the strings to be checked against

##checking for common substrings##
commonstring=[] #blank list to fill with longest common substring
for k in range(len(shortest)): #iterator to match length of shortest string
    for m in range(k,len(shortest)): #iterator to match above starting at each NT in string
        n=shortest[k:m+1] #store each substring of shortest string in N as loops
        found=False #boolean to swith if common substring found
        for p in complete: #p is each string in list of all strings
            if n in p: #if substring n is found in p
                found=True #indicate common substring found
            else: 
                found=False #if n is not in all strings p, not common
                break #end the foor loop for computational efficiency
        ##checking for longest common substring##
        if found and len(n)>len(commonstring): #if the substring is found in all DNA strings and is the longest substring found
            commonstring=n #store it as the common motif
print(commonstring) #print resulting longest commong substring
