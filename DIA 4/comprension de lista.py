palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)


pala = 'remoto'
lis = [letra for letra in pala]

print(lis)


numeros = [n if n%2==0 else "no" for n in range (0,21) ]
print(numeros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [p for p in valores if p%2==0]
#pares de la lista

pies = [10,20,30,40,50]
metros = [p* 3.281 for p in pies]
print(metros)