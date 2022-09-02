lista= ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice += 1



lista1 = ['a','b','c']

for item1 in enumerate(lista1):
    print(item1)

lista1 = ['a','b','c']

for indice,item1 in enumerate(lista1):
    print(indice,item1)


mis_tuples =list(enumerate (lista1))
print(mis_tuples)
