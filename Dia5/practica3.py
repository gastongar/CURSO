def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador+1] == 0:
            return True

        else:
            contador +=1

    return False



print(ceros_vecinos(5,6,7868,0,234,5,6734,23,6,7,1,23,5,76,78,0,1,0))