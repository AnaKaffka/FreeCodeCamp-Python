# Data structers
# Collections - permite que sejam armazenados vários valores em uma única 'variável'

friends = ['Joey', 'Rachel', 'Chandler', 'Ross']
print(friends)
gatos = ['Miu', 'Aika', 'Joe', 'Violeta']


for gato in gatos:
    print(gato)
print()
print(friends[1])
# mudar um item da lista
friends[3] = 'Monica'
print(friends)
print()

# len() tamanho da lista
print(len(gatos))
print()
#range function posição de um item na lista
print(list(range(5)))
print(list(range(len(gatos))))
print()
#Loop
for gato in gatos:
    print('Sou ', gato)

print()

for i in range(len(friends)):
    friend = friends[i]
    print('This is ', friend)
print()  