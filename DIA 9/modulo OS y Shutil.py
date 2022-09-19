import os

#import send2trash

print(os.getcwd())

archivo = open ('curso.txt', 'w')

archivo.write("Texto de Prueba")

archivo.close()

print(os.listdir())


#shutil.move("C:\\Users\\cti5680\\Desktop\\curso.txt , "" )


#send2trash,send2trash('curso.txt')

print(os.walk("C:\\Users\\cti5680\\Desktop\\CURSO\\DIA 9"))


ruta = "C:\\Users\\cti5680\\Desktop\\CURSO"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"en la capeta:{carpeta}")
    print(f"las subcarpetasson:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")
