from collections import defaultdict


def zero():
    return 0

letter_counts = defaultdict(lambda: 0)

with open('DATA/words.txt') as words_in:
    for line in words_in:
        letter = line[0]
        letter_counts[letter] += 1  # add 1 to previous value

print(letter_counts)


