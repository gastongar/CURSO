import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra)

patron = "ayuda"

busqueda = re.search(patron, texto)
todas = re.findall(patron, texto)

print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())


print(todas)
print(len(todas))

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())
