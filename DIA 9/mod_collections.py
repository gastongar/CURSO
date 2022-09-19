from collections import Counter

numeros = [8,6,9,4,5,8,5,6,4,7,8,5,9,5,3,5,8,6,3,2,]
print(Counter(numeros))

print(Counter("Misisipi"))


serie = Counter([1,1,1,1,1,3,3,3,3,6,6,6,6,7,8,8,8,8,9,9,9,9,9,])

print(serie.most_common(1))

print(list(serie))