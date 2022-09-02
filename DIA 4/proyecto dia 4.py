from random import *

'''adivinar un numeor entre el 1 y el 100 en  8 intentos
al adivinar decirle en cuantos intentos
preguntar el nombre
4 respuestas
menor a 1 o mayor a 100 ( respueta incorrecta
menor al secreo (informar menor
mayor informar mayor
'''

intentos = list(range(1,9))
#print(intentos)
numsecreto = randint(1, 101)
#print(numsecreto)
nombre = input(f"Hola vamos a adivinar un numero!! tienes 8 intentos"
               f" ¿ cuales es tu nombre ?:")
print(f" Buenisimo {nombre} vamos con el primer intento")
intento1 = 0

for tiro in intentos:
    if tiro > 0:
        intento1 = print(input(f"ingresa un numero de 1 a 100 :"))
        if intento1 !=  list(range(1,101)):
         print("El numero tiene que ser entre 1 y 100")
        else:
            if intento1==numsecreto:
                

        intentos = tiro - 1
    else:
       break







