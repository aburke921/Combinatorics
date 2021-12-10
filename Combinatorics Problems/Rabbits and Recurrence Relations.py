
def get_num_of_rabbit_pairs(n_months, k_rabbits_per_litter):

    prev1 = 1
    prev2 = 1

    for i in range(2, n_months):
        total_rabbit_pairs = prev1 + k_rabbits_per_litter * prev2
        prev2 = prev1
        prev1 = total_rabbit_pairs

    return total_rabbit_pairs


file = open('rosalind_fib.txt', 'r')
fileLines = file.read().split(" ")
n_months = int(fileLines[0])
k_rabbits_per_litter = int(fileLines[1])


total_rabbit_pairs = get_num_of_rabbit_pairs(n_months, k_rabbits_per_litter)
print(total_rabbit_pairs)
