
def hammingDistance(sequence1, sequence2):
    count = 0
    for index in range(len(sequence1)):
        if sequence1[index] != sequence2[index]:
            count += 1
    print(count)


file = open('rosalind_hamm.txt', 'r')
fileLines = file.read().split()

givenString1 = fileLines[0]
givenString2 = fileLines[1]

hammingDistance(givenString1, givenString2)