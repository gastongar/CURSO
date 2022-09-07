#def suma(**kwargs):
#    print(type(kwargs))


#def suma(**kwargs):
#    total = 0
#    for clave,valor in kwargs.items():
#        print(f"{clave} = {valor}")
#        total += valor
#    return total


def suma2(num1,num2,*args,**kwargs):
    print(f"el primer var es{num1}")
    print(f"el segundo valor es {num2}")
    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave}={valor}")


suma2(15,50,10,200,4000,44763,x="uno", y ="dos" , z='tres')


#print(suma(x=3, y=5, z=9))