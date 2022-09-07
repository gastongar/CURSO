import random
"""Palbras del juego"""
palabras=["mango", "banana", "cereza", "ciruela", "pomelo"]

"""elegir una palabra"""
def elegir_palabra(names):
       return random.choice(names)




""" elegir palabra y contar letras"""
word=elegir_palabra(palabras)
largo = len(word)

print(word)
print(largo)
