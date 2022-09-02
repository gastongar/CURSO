menor=min(58,96,72,64,35,)
maximo=max(58,96,72,64,35,)
print(menor)
print(maximo)

lista = [58,96,72,64,35]
print(max(lista))
print(f" el menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ['juan','pablo','alicia','carlos']

print(min(nombres))

nombre = "Carlos"
#distingue minusculas (buscar primero may)
print(min(nombre.lower()))

dic = {'c1':45,'c2':11}
#valor minimo es "c1"
print(min(dic))

dic = {'c1':45,'c2':11}
#para traer el de valor minimo  para traer el 11
print(min(dic.values()))