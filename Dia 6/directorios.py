import os
from pathlib import Path

carpeta = Path('C:/Users/garab/OneDrive/Documentos/CURSO')
archivo = carpeta / 'alternativo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

otra = Path('/Users/garab/OneDrive/Documentos/CURSO') / 'nativo.txt'
print(otra.read_text())


esto = os.path.basename(otra)

print(esto)

