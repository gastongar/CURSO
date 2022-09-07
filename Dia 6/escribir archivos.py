mi_archivo = open('prueba1.txt',"w")

mi_archivo.write('soy el nuevo texto\n')

mi_archivo.write('otro texto')

lista=['otro texto','mundo','aqui','estoy']

for p in lista:
    mi_archivo.writelines(p + '\n')




mi_archivo.close()