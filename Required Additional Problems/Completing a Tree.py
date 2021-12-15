
#completing a tree
#background problem for counting phylogenetic ancestors


treeData = []                                          
with open("rosalind_tree.txt", "r") as file:
    for line in file:                                 
        split_data = [int(x) for x in line.split()]
        treeData.append(split_data)                    

n = treeData[0][0]                                     
edges = treeData[1: ]                                   
print(n - len(edges) - 1)     
