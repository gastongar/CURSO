#comparaciones  OP LOGICOS
# and or not

mi_b = 4<5<6
print(mi_b)

mi_b2 = 4<5>6
print(mi_b2)

mi_b3= (4<5) and (5==3+2)
print(mi_b3)

mi_b4= 10==10 or (5==7+2)
print(mi_b4)

texto= 'esta frase es breve'
mi_b5= 'frase' in texto and 'breve' in texto
print(mi_b5)

mi_b6= not 'a'=='a'
print(mi_b6)



