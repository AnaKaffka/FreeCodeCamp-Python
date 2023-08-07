"""    
#open a file
print('cada linha:')
xfile = open('xxx.txt')
for cheese in xfile:
    print(cheese) #vai imprimir cada linha


#contar o número de linhas de um arquivo
print()
print("Numero de linha:")
fhand = open('xxx.txt')
count=0
for line in fhand:
    count=count+1
print('Line count: ', count)    

#ler o arquivo inteiro
print()
print('total caracteres')
fhand=open('xxx.txt')
inp = fhand.read()
print(len(inp)) #total de caracteres

# search em um arquivo
print()
fhand = open('xxx.txt')
for line in fhand:
    if line.startswith('Neil'):
        print(line)
print()        
# apagar quebra delinha \n
print('texto sem pular linha \n')
fhand = open('xxx.txt')
for line in fhand:
    line = line.rstrip()
    print(line)

# Skipping with continue \n
print()
print('Skipping with continue: \n')
fhand = open('xxx.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line) 
print()
# Usando in operator
print('Usando in operator \n')
fhand = open('xxx.txt')
for line in fhand:
    line = line.rstrip()
    if not 'From:' in line :
        continue
    print(line)


# pedir para o usuario selecionar o arquivo
fname = input('Enter the file name: ')
fhand = open(fname)
count=0
for line in fhand:
    if line.startswith('From:') :
        count = count + 1
print('There were ', count, ' From: lines in ',fname)        
"""
# pedir para o usuario selecionar o arquivo evitar que o usuário não fale o arquivo certo (ou qlqr coisaque não sejaum arquivo)
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except: 
    print('File cannot be openned:', fname)
    quit() #desliga o programa

count=0
for line in fhand:
    if line.startswith('From:') :
        count = count + 1
print('There were ', count, ' From: lines in ',fname)   