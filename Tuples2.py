'''
#Sorting tuples
d = {'a':10, 'c':22, 'b':1}
print(d.items())
sorted(d.items())
print(sorted(d.items()))

for k, v in sorted(d.items()):
    print(k, v)

#Sorting by values instead of key descending order

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
'''
#Achar as 10 palavras mais comuns
fhand = open('ring.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

lst = list()
for key, val in counts.items():
    newtop = (val, key)
    lst.append(newtop)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)
print()
# versão mais curta 
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))
