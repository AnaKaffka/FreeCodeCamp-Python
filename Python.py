x = 2
print (x)
if x <= 2:
    print("Yes")

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There') #this does not print out
except:
    istr = -1
print('Done',istr)     

def thing() : #função
    print('Aika')
    print('Miudo')
    print('Johnny')
    print('Violeta')

thing()

def conta (x,y) :
    w = x+y
    print(w)

conta(1,2)
#Loops and Iterations
print('While loop')
#While indefinite loop
n=1
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print(n)    

print('While com break:')
#while com break
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n+1

print('While com continue e break')
#While com continue e break
""""
n=10
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('done!')    

"""
# for loop definite loop
print('for loop')

for i in [2,1,5]:
    print(i)

#
smallest = None
print("before: ", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar,smallest)
print("Smallest:", smallest)    


#More Patterns
# count
count=0
print('before', count)
for thing in [9, 41, 12, 3, 74, 15]:
    count = count+1
    print(count, thing)
print("after", count)    

# soma
sum = 0
print("Before:", sum)
for thing in [9, 41, 12, 3, 74, 15]:
    sum = sum+thing
    print(sum, thing)
print('After', sum)    

# média
count = 0
sum = 0
print('before:', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count +1
    sum= sum +value
    print(count, sum, value)
print('After: ', count, sum, sum/count) 

# procurar valores específicos
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value >20:
        print("Large number", value)
    else:
        print("False")
print("After")    

# descobrir se existe uma variavel especifica
found = False
print("before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found=True
    print (found, value)
print('After', found)        
