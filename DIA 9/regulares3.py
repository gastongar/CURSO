import re

clave= input("CLAVE:")


patron= r'\D{1}\w\{7}'

chequear= re.search(patron, clave)

print(chequear)

texto= " no atendemos los lunes a la tarde"

buscar= re.search(r'lunes|martes', texto)
buscar2=re.search(r'....demos',texto)
buscar3=re.search(r'^\D',texto)
buscar4=re.search(r'\D$', texto)

print(buscar3)
print(buscar)
print(buscar2)