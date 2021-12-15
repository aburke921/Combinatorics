

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

FASTAs = [fileLines[FASTA][1:] for FASTA in range(0, len(fileLines), 2)]
sequences = [fileLines[sequence] for sequence in range(1, len(fileLines), 2)]

s, t = getEdges(FASTAs, sequences, 3)

for i in range(len(s)):
    print(s[i] + " " + t[i])

