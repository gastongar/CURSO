mi_archivo = open('prueba1.txt',"a")

mi_archivo.write('soy el nuevo texto\n')

mi_archivo.write('bienvenido ')

lista=['otro texto','mundo','aqui','estoy']

for p in lista:
    mi_archivo.writelines(p + '\n')
