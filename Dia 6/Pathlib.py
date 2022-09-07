from pathlib import Path, PureWindowsPath
"""path abre y cierra archivo"""
carpeta = Path('C:/Users/garab/OneDrive/Documentos/CURSO/nativo.txt')

ruta_w = PureWindowsPath(carpeta)
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)
print(carpeta.absolute())
print(ruta_w)

if not carpeta.exists():
    print( "este archino no exixte")
else:
    print("genial, existe")

