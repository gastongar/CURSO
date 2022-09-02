lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

#Crea un loop For a lo largo de la siguiente lista de números,
# imprimiendo en pantalla cada uno de sus elementos,
# e interrumpe el flujo en el momento que encuentres un valor negativo:

#print(type(lista_numeros))

for numero in lista_numeros:
    if numero < 0:
        break
    else:
        print(numero)




