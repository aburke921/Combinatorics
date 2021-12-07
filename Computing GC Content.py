def maxGC_Content(fileName):

    file = open(fileName, 'r')

    GC_Counter = {}
    id = ''
    totalSequenceLength = 0
    totalGandCs = 0
    for line in file:
        line = line.strip('\n')

        if  line[0] == '>':
            if id != '':
                GC = (totalGandCs * 100) / (totalSequenceLength)
                GC_Counter[id] = GC

            id = line[1:]

            totalSequenceLength = 0
            totalGandCs = 0
        else:
            totalSequenceLength += len(line)
            totalGandCs += line.count('G') + line.count('C')

    GC = (totalGandCs * 100) / (totalSequenceLength)
    GC_Counter[id] = GC


    file.close()

    maxGC = max(GC_Counter.values())

    for key, value in GC_Counter.items():
        if value == maxGC:
            print(key)
            print(format(value, '.6f'))

maxGC_Content('rosalind_gc.txt')
