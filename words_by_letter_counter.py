from collections import Counter

first_letter_counts = Counter()
all_letter_counts = Counter()

with open('DATA/words.txt') as words_in:
    for line in words_in:
        letter = line[0]
        first_letter_counts[letter] += 1  # add 1 to previous value
        for letter in line.rstrip():
            all_letter_counts[letter] += 1

print(first_letter_counts)
print()
print(first_letter_counts.most_common(5))
print()
print(all_letter_counts)
# etoindrshldu


