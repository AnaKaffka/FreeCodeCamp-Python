"""
#concatenating
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print()
print(a)

#Slicing (último número não incluso) uptobut not including
t=[9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
print()
#Métodos lista
x=list()
print(type(x))
print(dir(x))
"""
# Construindo uma lista do zero
stuff=list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
print()
# in operator
some=[1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print (20 not in some)

# Sorting 
friends =['Rachel', 'Ross', 'Monica', 'Joey', 'Chandler', 'Phoebe']
friends.sort()
print(friends)
print(friends[1])
print()
some.sort()
print(some)
print()
#Build-in Functions ands Lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#colocando inputs em uma lista:
total=0
count=0
while True:
    inp = input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)    
print()
# Mesma coisa de outro jeito ^
numlist = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average:', average)    
print()