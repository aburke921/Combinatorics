
def get_num_of_rabbit_pairs(n_months, m_rabbit_life_length):
    rabbit_pairs = [1, 1]
    months = 2
    count = []

    while months < n_months:

        if months < m_rabbit_life_length:
            bunny_count = rabbit_pairs[-2] + rabbit_pairs[-1]
        elif months == m_rabbit_life_length or count == m_rabbit_life_length + 1:
            bunny_count = rabbit_pairs[-2] + rabbit_pairs[-1] - 1
        else:
            bunny_count = rabbit_pairs[-2] + rabbit_pairs[-1] - rabbit_pairs[-(m_rabbit_life_length + 1)]

        rabbit_pairs.append(bunny_count)
        months += 1

    total_rabbit_pairs = rabbit_pairs[-1]

    return total_rabbit_pairs


file = open('rosalind_fibd.txt', 'r')
fileLines = file.read().split(" ")

n_months = int(fileLines[0])
m_rabbit_life_length = int(fileLines[1])


total_rabbit_pairs = get_num_of_rabbit_pairs(n_months, m_rabbit_life_length)
print(total_rabbit_pairs)