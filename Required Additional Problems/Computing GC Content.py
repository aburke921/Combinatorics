




#rosalind 10

def GCcontent(string):
    temp = (string.count("G") + string.count("C"))/len(string)
    return temp

s = {}
a = None
place = 0

with open('rosalind_gc.txt', 'r') as f:
    
    iden = None
    string = None
    
    while True:
        read=f.readline().strip()
        if not read:
            s[iden]=GCcontent(string)
            if s[iden] > place:
                a = iden
                place = s[iden]
            break
        else:
            if read.startswith(">"):
                if iden is not None:
                    s[iden] = GCcontent(string)
                    if s[iden] > place:
                        a = iden
                        place = s[iden]
                iden = read[1: ]
                string = ""
            else:
                string += read

print(a, f"{s[a]*100}", sep = '\n')
