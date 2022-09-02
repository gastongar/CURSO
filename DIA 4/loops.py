lista = ['a','b','c']

for letra in lista:
    print(letra)

lista = ['a', 'b', 'c']

for letra in lista:
    print("Letra: " +letra)

lista = ['a', 'b', 'c']

for letra in lista:
    nunero_letra = lista.index(letra) + 1
    print(f"Letra {nunero_letra}:{letra}")


lista2 = ['pablo', 'laura', 'fede','luis','julia']

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("Nombre que no comienza con L")


numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)


palabra = 'python'

for letr in palabra:
    print(letr)









