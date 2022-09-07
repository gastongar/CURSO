from random import shuffle
#Lista Inicial
palitos =['-','--','---','----']



# mezclar palitos
def mezclar(lista):
    print(lista)
    shuffle(lista)
    print(lista)
    return lista


#pedir intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input (" elige un numero del 1 al 4: ")

    return int(intento)


# comprobar intento
def chequer_intento(lista,intento):
    if lista[intento -1] == '-':
        print("A lavar los platos")
    else:
        print("esta vez zafaste")

    print(f"te ha tocado {lista[intento-1]}")


palitos_mezclados =mezclar(palitos)
seleccion = probar_suerte()
chequer_intento(palitos_mezclados,seleccion)