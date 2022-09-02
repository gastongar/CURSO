from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)

nombre = input("dime tu nombre: ")
print(f"Bueno {nombre}, he pensado un numero en 1 y 100 \n Tienes 8 intentos para adivina")

while intentos < 8:
    estimado = int(input(" cual es el numero?: "))
    intentos +=1
    if estimado not in range(1,100):
        print("El numero elegido no esta en el rango 1 a 100")
    if estimado < numero_secreto:
        print("mi numero es mas alto")
    if estimado > numero_secreto:
        print("mi numero es mas bajo")
    if estimado == numero_secreto:
        print(f"Felicitaciones!! {nombre} Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. el numero secreto era {numero_secreto}")
