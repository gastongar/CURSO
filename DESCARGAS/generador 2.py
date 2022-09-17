def mi_gen():
    x = 1
    yield x

    x += 1
    yield x

    x+= 1
    yield x

g=mi_gen()



print(next(g))
print(next(g))
print(next(g))
