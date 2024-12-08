#Use sorted() function
tobuy = {}


while True:
    try:
        item = str(input()).upper()

    except EOFError:
        print("")
        break

    else:
        if item not in tobuy:
            tobuy[item] = 1
        else:
            tobuy[item] += 1


#Aquí imprimir por pantalla el dictionario por orden alfabético y contabilizado
for item in sorted(tobuy.keys()):
    print(tobuy[item], item)
