from pathlib import Path

base = Path.home()
guia = Path(base,"Europa","Espania", Path("Barcelona", "Sagrada_Familia.txt"))
print(base)
print(guia)

guia2= guia.with_name("La_Pedrera.txt")
print(guia2.parent)



