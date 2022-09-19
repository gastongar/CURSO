from collections import defaultdict

mi_dic = {"uno":"verde","dos":"azul", "tres":"rojo", "edad": 44 }

print(mi_dic["edad"])


dic = defaultdict(lambda: "nada")
dic['cuatro']= 'verde'
print(dic['cinco'])
print(dic['siete'])
print(dic)


