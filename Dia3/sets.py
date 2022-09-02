mi_set= set([1,2,3,4,5,1,1,1,1,2,2,5,5,])
print(type(mi_set))
print(mi_set)

otro_set= {1,2,(1,2,3),3}
print(type(otro_set))
print(otro_set)

print(len(mi_set))
print(2 in mi_set)

s3=mi_set.union(otro_set)

print(s3)

mi_set.add(6)
mi_set.remove(4)
mi_set.discard(7)
sorteo=mi_set.pop()
s3=mi_set.union(otro_set)
print(sorteo)
print(s3)

s3.clear()

print(s3)

