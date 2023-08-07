"""
# exercicio
counts = {'chuck':1, 'annie':42, 'jan':100}
for key in counts:
    if counts[key]>10:
        print(key, counts[key])


#Counting Pattern
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words: ', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) +1
print('Counts', counts)    
print()

#Definite loops and Dictionaries
counts = {'chuck':1, 'fred':42, 'jan':100}
for key in counts:
    print(key, counts[key])
print()

#Retrieving lists of Keys and Values
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())
print()

#Two Iteration Variables!
for aaa, bbb in counts.items():
    print(aaa, bbb)
print()    
"""
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
