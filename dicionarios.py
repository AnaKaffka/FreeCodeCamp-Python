#exercício
"""
dict = {"fri": 20, "Thu": 6, "Sat": 1}
print(dict)
dict["Thu"] = 13
dict["Sat"] = 2
dict["Sun"] = 9
print(dict)

#Dicionários -  Conjunto de elementos não ordenados que tem uma key(chave) para retornar ao elemento
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print()
print(purse['candy'])
purse['candy'] = purse['candy'] +2
print(purse)

#Exercício
counts={'quincy':1,'mrugesh':42, 'beau':100, '0':10}
print(counts.get('kris', 0))
"""

#Common applications
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] +1
print(counts)            
print()
# get method for dictionaries
if name in counts:
    x = counts[name]
else :
    x = 0
x = counts.get(name, 0)    
print(x)
