
lista_numeros = [1,2,15,7,2]

def reducir_lista (lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista



def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio


lista =reducir_lista(lista_numeros)
final =promedio(lista)
print(lista)
print(final)

