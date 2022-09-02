texto=input("por favor ingresa un texto:").lower()
le1=input("por favor ingresa una primera letra:").lower()
le2=input("por favor ingresa una segunda letra:").lower()
le3=input("ahora si ingresa la ultima letra:").lower()

#cuantas veces aparecen cada una de las letras#
veces1=texto.count(le1)
veces2=texto.count(le2)
veces3=texto.count(le3)
print("la primera letra aparace",[veces1])
print("la segunda letra aparace",[veces2])
print("la ultima letra aparace",[veces3])
#cuantas palabras#
palabras=texto.split(" ")
print("La cantidad de palabras del texto es: ",len(palabras))
#Primer y Ultima Letra del texto
print("la pimer letra del texto es: ", texto[0])
print("la ultima letra del texto es:", texto[-1])
#orden inverso
print("el orden inverso del texto es: ",texto[::-1])
#decir si esta python
esta=("python" in texto)
print(esta)


