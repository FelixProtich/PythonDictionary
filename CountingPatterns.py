counts = dict()
line = input('Enter a line of texts: ')
words = line.split()

print('words:', words)
print('counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)
