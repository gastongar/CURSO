texto="Este es el texto de Gaston"
resultado= texto.split(" ")
print(resultado)

resultado2= texto[2].upper()
print(resultado2)


a="Aprender"
b="Python"
c="es"
d="Genial"
e= " - ".join([a,b,c,d])
print(e)


texto="Este es el texto de Gaston"
resultado= texto.find("e")
print(resultado)


texto="Este es el texto de Gaston"
resultado= texto.replace("texto","curso").replace("Gaston","Pedro")
print(resultado)

