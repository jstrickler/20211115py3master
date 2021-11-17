
letter_counts = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        letter = line[0]
        if letter not in letter_counts:
            letter_counts[letter] = 0  # add letter to dict

        letter_counts[letter] += 1  # add 1 to previous value
        #  letter_counts[letter] = letter_counts[letter] + 1

print(letter_counts)


