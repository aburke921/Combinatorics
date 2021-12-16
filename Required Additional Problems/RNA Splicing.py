

def translate_RNA_into_protein(RNA):

    aminoAcids = {
        'UUU': 'F', 'UUC': 'F',
        'UUA': 'L', 'UUG': 'L',

        'CUU': 'L', 'CUC': 'L',
        'CUA': 'L', 'CUG': 'L',

        'AUU': 'I', 'AUC': 'I',
        'AUA': 'I', 'AUG': 'M',

        'GUU': 'V', 'GUC': 'V',
        'GUA': 'V', 'GUG': 'V',

        'UCU': 'S', 'UCC': 'S',
        'UCA': 'S', 'UCG': 'S',

        'CCU': 'P', 'CCC': 'P',
        'CCA': 'P', 'CCG': 'P',

        'ACU': 'T', 'ACC': 'T',
        'ACA': 'T', 'ACG': 'T',

        'GCU': 'A', 'GCC': 'A',
        'GCA': 'A', 'GCG': 'A',

        'UAU': 'Y', 'UAC': 'Y',

        'CAU': 'H', 'CAC': 'H',
        'CAA': 'Q', 'CAG': 'Q',

        'AAU': 'N', 'AAC': 'N',
        'AAA': 'K', 'AAG': 'K',

        'GAU': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E',

        'UGU': 'C', 'UGC': 'C',
        'UGG': 'W',

        'CGU': 'R', 'CGC': 'R',
        'CGA': 'R', 'CGG': 'R',

        'AGU': 'S', 'AGC': 'S',
        'AGA': 'R', 'AGG': 'R',

        'GGU': 'G', 'GGC': 'G',
        'GGA': 'G', 'GGG': 'G'
    }

    startLocation = 0
    stopLocation = len(RNA)


    protein = ""
    for index in range(startLocation, stopLocation - 3, 3):
        sequence = RNA[index: index+3]
        protein += aminoAcids.get(sequence)

    return protein


def transcribe_DNA_into_RNA(DNA):
    RNA = DNA.replace('T', 'U')
    return RNA


file = open('rosalind_splc.txt', 'r')
fileLines = file.read().strip().split(">")

fileLines = fileLines[1:]

lines = []
for line in fileLines:
    lines.append(line[13:].replace('\n',''))


DNA = lines[0]
introns = lines[1:]

for intron in introns:
    DNA = DNA.replace(intron, "")


RNA = transcribe_DNA_into_RNA(DNA)

protein = translate_RNA_into_protein(RNA)
print(protein)
