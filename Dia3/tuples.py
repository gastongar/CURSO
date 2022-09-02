mi_tuple = (1,2,3,(10,20),4)
t = (5,5.6,"f",5)

print(type(mi_tuple))

print(mi_tuple[-2][0])

mi_tuple =list(mi_tuple)

print(type(mi_tuple))

mi_tuple= tuple(mi_tuple)


print(type(mi_tuple))


x,y,z,w=t

print(x,y,z)

print(len(t))
print(t.count(5))
print(t.index(5))





