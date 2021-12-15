def wordCount(str):
    symbolCount = {}

    for symbol in str:
        symbolCount[symbol] = symbolCount.get(symbol, 0) + 1

    print(symbolCount.get('A'), symbolCount.get('C'), symbolCount.get('G'), symbolCount.get('T'))


string=open("rosalind_dna.txt").readlines()
sequence=string[0]

wordCount(sequence)