def hammingDistance(sequence1, sequence2):
    count = 0
    for index in range(len(sequence1)):
        if sequence1[index] != sequence2[index]:
            count += 1
    print(count)

file = open('file', 'r')

givenStrings = file.readlines()

hammingDistance(givenStrings[0], givenStrings[1])