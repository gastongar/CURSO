nombre=input("Dime tu nombre:")
ventas=input("cuantos has vendido este mes:")
ventasf=round(float(ventas)*13/100,2)

print(f"{nombre} el monto de la comision por las ventas de este mes es de {ventasf}")