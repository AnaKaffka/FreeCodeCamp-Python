"""
for n in "banana":
    print(n)
print()
print()
#Looking inside the strings
fruit = 'banana'
letter = fruit[0]
print(letter)

x = 3
w = fruit[x-1]
print(w)


print()
print()
# para saber o tamanho da string
print(len(fruit))

print()
print()

# loop com string sabera posição de cada letra

index=0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index +1


#For loop
for letter in fruit:
    print(letter)
print()
print()
# contar quantas vezes x letra aparece
word = 'banana'
count=0
for letter in word:
    if letter =='a':
        count = count + 1
print(count)        

print()
print()

# proximo video
#Slicing Strings pegandopedaços da string ':' -> até não inclui o último
s="Monty Python"
print(s[0:4])
print(s[6:7])
print(s[6:20])
print()
print(s[:2])
print(s[8:])
print(s[:])
print ()
print()
# Concatenation
a = 'Hello'
b = a + 'there'
print(b)

c = a + ' ' + 'There'
print(c)

print()
print()
# usando in como operador lógico

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit :
    print('Found it!')
   
#comparar strings
word = 'banana'
if word =='banana':
    print('all right, bananas') 

word = 'abacaxi'    
if word < 'banana':
    print('your word, ' + word + ', comes before banana.')   

#
word = 'bananana'
i = word.find("na")
print(i)

# String Library lower() = deixar em lower case
greet = 'HELLO BOB'
zap = greet.lower()
print(zap)

print('Hi, There'.lower())
stuff='hello world'

#Find()
pos=stuff.find('ll')
print(pos)
   """
#Search and replace
greet='Hello bob'
"""
nstr=greet.replace('bob', 'Jane')
print(nstr)
nstr = greet.replace('o','X')
print(nstr)
greet.lstrip()
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())
"""
print(greet.startswith('Hello'))
print(greet.startswith('llo'))
