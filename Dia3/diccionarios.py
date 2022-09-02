diccionario= {"c1":"valor1", "c2":"valor2"}
print(diccionario)

resultado=diccionario["c1"]
print(resultado)

cliente={"nombre":"juan","apellido":"Fuentes","peso":88,"talla":1.76}
consulta=(cliente["apellido"])
print(consulta)
altura=(cliente["talla"])
print(altura)

dic= {"d1":55,"d2":[10,20,30],"d3":{"s1":100,"s2":200}}
print(dic["d2"])
print(dic["d2"][1])
print(dic["d3"]["s1"])

dic2= {"f1":["a","b","c"],"f2":["d","R","f"],"f3":"r"}
print(dic2["f2"][1].lower())
dic2["f4"]="h"
print(dic2)

dic2["f3"]=1

print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.items())


