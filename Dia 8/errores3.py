"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def suma(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("Error inesperado")

suma(1,"papas")