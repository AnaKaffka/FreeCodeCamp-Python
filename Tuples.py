#Nas listas usa-se [] já nas tuplas ()
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(y)
print(max(y))

#Tuples são imutaveis!! não se pode alterar o conteúdo!
#Dá para usar tuples como (x, y) = (99, 98)
# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items() :
    print(k, v)
tups = d.items()
print(tups)    
#Tuplas são comparáveis
print((0, 1, 2) < (5, 1, 2))
#Exercício
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k,i)