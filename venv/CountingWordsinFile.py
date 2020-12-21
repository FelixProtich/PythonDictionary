#open file

name = input('Enter filename: ')
handle = open(name)

try:
    handle = open(name)
except:
    print("File do not exist: ", name)
    quit()

#Splitting and counting words of a line

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#Looking for bigword and bigcount

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count> bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
