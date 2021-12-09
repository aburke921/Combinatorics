

'''

    Always starts with M --> AUG

    W = 1 way
    Y = 2 ways
    C = 2 ways
    E = 2 ways
    K = 2 ways
    Q = 2 ways
    S = 6 ways
    L = 6 ways
    R = 6 ways
    G = 4 ways
    F = 2 ways
    D = 2 ways
    H = 2 ways
    N = 2 ways
    M = 1 way
    A = 4 ways
    P = 4 ways
    T = 4 ways
    V = 4 ways
    I = 3 ways

    3 Stop Codons


'''

def get_num_of_ways_translated(protein):

    ways_to_get_amino_acid = {
        'W' : 1, 'Y' : 2, 'C' : 2, 'E' : 2, 'K' : 2, 'Q' : 2, 'S' : 6, 'L' : 6, 'R' : 6, 'G' : 4, 'F' : 2, 'D' : 2,
        'H' : 2, 'N' : 2, 'M' : 1, 'A' : 4, 'P' : 4, 'T' : 4, 'V' : 4, 'I' : 3
    }

    total_num_of_ways = 1

    for amino_acid in protein:
        total_num_of_ways = total_num_of_ways * ways_to_get_amino_acid.get(amino_acid)
        total_num_of_ways = total_num_of_ways % 1000000

    total_num_of_ways = total_num_of_ways * 3 # To take into account the stop codons
    total_num_of_ways = total_num_of_ways % 1000000

    print(total_num_of_ways)


file = open('rosalind_mrna.txt', 'r')
protein = file.read().split()[0]

get_num_of_ways_translated(protein)


