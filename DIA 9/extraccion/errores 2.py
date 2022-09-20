def pedir_numero():
    while True:
        try:
            numero = int(input("dame un numero: "))
        except:
            print("ese no es un numero")
        else:
            print(f"ingresaste el numero {numero}")
            break
    print("gracias")


pedir_numero()