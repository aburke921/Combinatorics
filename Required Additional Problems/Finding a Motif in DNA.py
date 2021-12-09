
def get_substr_locations(full_string, desired_substring):

    locations = ''
    for index in range(len(full_string)):

        if index + len(desired_substring) <= len(full_string):
            substring = full_string[index: index + len(desired_substring)]

            if substring == desired_substring:
                locations = locations + str((index + 1)) + ' '

    return locations


file = open('rosalind_subs.txt', 'r')
lines = file.read().split()
full_string = lines[0]
desired_substring = lines[1]

locations = get_substr_locations(full_string, desired_substring)

print(locations)
