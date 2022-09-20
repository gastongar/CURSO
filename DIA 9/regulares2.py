import re


texto= "llama al 564-453-1554 ya mismo"

patron = r"\d\d\d-\d\d\d-\d\d\d\d"
patron2= r'\d{3}-\d{3}-\d{4}'
patron3= re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron,texto)
resul2 = re.search(patron3,texto)
print(resultado)
print(resultado.group())

print(resul2.group(2))



