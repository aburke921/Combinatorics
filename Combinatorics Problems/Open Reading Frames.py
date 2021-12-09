
def reverseCompliment(DNA):
    reverseComp = ''
    for letterPos in range(len(DNA)):

        letter = DNA[len(DNA) - letterPos - 1]

        if letter == 'A':
            compLetter = 'T'
        elif letter == 'T':
            compLetter = 'A'
        elif letter == 'C':
            compLetter = 'G'
        else:
            compLetter = 'C'

        reverseComp += compLetter

    return reverseComp


def OpenReadingFrames(DNA):

    reversedDNA = reverseCompliment(DNA)

    RNA1 = transcribe_DNA_into_RNA(DNA)
    RNA2 = transcribe_DNA_into_RNA(reversedDNA)

    reading_frames1 = get_all_reading_frames(RNA1)
    reading_frames2 = get_all_reading_frames(RNA2)

    reading_frames = reading_frames1 + reading_frames2
    cleaned_reading_frames = []

    # Removes duplicates and reading frames that have nothing in them
    for frame in reading_frames:
        if cleaned_reading_frames.count(frame) == 0 and frame != []:
            cleaned_reading_frames.append(frame)

    for frame in cleaned_reading_frames:
        # print('reading_frame: ', frame)
        protein = translate_codons_into_protein(frame)
        print(protein)





def transcribe_DNA_into_RNA(DNA):
    RNA = DNA.replace('T', 'U')
    return RNA


def get_codons_in_frame(RNA):
    list_of_codons = [RNA[y - 3:y] for y in range(3, len(RNA) + 3, 3)]
    return list_of_codons


def get_codons_until_stop_codon(codons):
    stop_locations = []

    if codons.count('UAA') > 0:
        stop_locations.append(codons.index('UAA'))

    if codons.count('UAG') > 0:
        stop_locations.append(codons.index('UAG'))

    if codons.count('UGA') > 0:
        stop_locations.append(codons.index('UGA'))

    if len(stop_locations) != 0:
        return codons[:min(stop_locations)]

    return []



def get_all_reading_frames(RNA):

    num_of_starts = RNA.count('AUG')
    start_location = -1
    reading_frames = []

    for readingFrame in range(num_of_starts):

        start_location = RNA.index('AUG', start_location + 1)
        codons = get_codons_in_frame(RNA[start_location:])
        reading_frame = get_codons_until_stop_codon(codons)

        reading_frames.append(reading_frame)

    return reading_frames



def translate_codons_into_protein(list_of_codons):

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

    protein = ""
    for codon in list_of_codons:
        protein += aminoAcids.get(codon)

    return protein



file = open('rosalind_orf.txt', 'r')
fileLines = file.readlines()

DNA = ""

for line in fileLines[1:]:
    DNA = DNA + line.strip('\n')

OpenReadingFrames(DNA)
