def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n > 0:
            return True
        else:
            return False


lista_numeros =([10,35,465,5,15,98])



print(todos_positivos)