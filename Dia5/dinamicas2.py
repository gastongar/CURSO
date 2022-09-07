def suma_menores(lista_numeros):
    sumados=[]
    for n in lista_numeros:
        if n in range(1,1000):
            sumados.append(n)
            sum(sumados)
        else:
            pass

lista_numeros=[-5,325,500,54,1500,36,2250] 
resultado = suma_menores(lista_numeros)
print(resultado)