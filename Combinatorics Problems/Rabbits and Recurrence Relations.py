string=open("rosalind_fib.txt").readlines() #import Rosalind file
split=string[0].split() #pull the first line from the file and store it in 'split'
months=int(split[0]) #store the n value in 'months'
littersize=int(split[1]) #store the k value in 'littersize'
lastmonthbreeding=0
lastmonthtotal=1
for i in range (months-1): 
    currentbreeding=lastmonthtotal
    # print(lastmonthtotal)
    currenttotal=lastmonthbreeding*littersize+lastmonthtotal
    lastmonthbreeding=currentbreeding
    lastmonthtotal=currenttotal
totalpairs=lastmonthtotal
print(totalpairs) #print result