

def getEdges(FASTAs, sequences, k):
    s = []
    t = []

    for fastaIndex in range(len(FASTAs)):
        for sequenceIndex in range(len(sequences)):

            if fastaIndex != sequenceIndex:
                if sequences[fastaIndex][-k:] == sequences[sequenceIndex][:k]:
                    s.append(FASTAs[fastaIndex])
                    t.append(FASTAs[sequenceIndex])

    return s, t


file = open('rosalind_grph.txt', 'r')
fileLines = file.read().split()

FASTAs = [fileLines[FASTA][1:] for FASTA in range(0, len(fileLines), 3)]
sequences1 = [fileLines[sequence] for sequence in range(1, len(fileLines), 3)]
sequences2 = [fileLines[sequence] for sequence in range(2, len(fileLines), 3)]

sequences = []
for sequence in range(len(sequences1)):
    sequence1 = sequences1[sequence]
    sequence2 = sequences2[sequence]
    fullSequence = sequence1 + sequence2
    sequences.append(fullSequence)


data = {FASTAs[index]:sequences[index] for index in range(len(FASTAs))}

s, t = getEdges(FASTAs, sequences, 3)

for i in range(len(s)):
    print(s[i] + " " + t[i])

