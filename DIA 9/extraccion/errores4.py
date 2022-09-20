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


def cociente(num1, num2):
     try:
      print(num1 / num2)
     except TypeError:
      print("Los argumentos a ingresar deben ser números")
     except ZeroDivisionError:
      print("El segundo argumento no debe ser cero")


cociente(10,2)
# MENSAJE EN PANTALLA

