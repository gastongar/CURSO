suma_cuadrados = (1, 2, 3)


def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg ** 2

    return suma


def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)

    return suma