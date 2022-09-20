def suma():
    n1 = int(input("numero1: "))
    n2 = int(input("numero2: "))
    print(n1+n2)
    print("gracias por sumar")




try:
    # Codigo a probar
    suma()
except:
    # Codigo a ejecutar si hay error
    print("algo no ha salido bien")
else:
    #codigo a ejecutar si no hay error
    print("hiciste todo bien")

finally:
    # codigo a ejecutar de todos modos
    print("eso fue todo")

