import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()
ruta="C:\\Users\\cti5680\\Desktop\\CURSO\\DIA 9\\proyectodia9\\Mi_Gran_Directorio"
patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
num_encontrados = []
arch_encontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), patron)
            if resultado != '':
                num_encontrados.append((resultado.group()))
                arch_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in arch_encontrados:
        print(f'{a}\t{num_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados: {len(num_encontrados)}')
    print()
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la Busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)

crear_listas()
mostrar_todo()




