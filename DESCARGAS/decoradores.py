
def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())


    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula

    elif tipo == "min":
        return minuscula


operacion = cambiar_letras("may")

operacion("palabra")


#print("hola")
#mayuscula("hoy es lunes")
#print("adios")


#mi_funcion = mayuscula

#mi_funcion("python")


#def una_funcion(funcion):
#    return funcion


#una_funcion(mayuscula("probando"))