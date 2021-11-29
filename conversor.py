
# pesos a dolares
pesos = input("cuantos pesos colombianos tienes? : ")
pesos = float(pesos)

valor_dolar= 4000

dolares = pesos/valor_dolar
dolares = round(dolares, 21)
dolares = str(dolares)

print("Tienes  $ "+ dolares + " dolares")


# dolares a pesos
dolares1 = input ("cuantos dolares tienes? : ")
dolares1 = float(dolares1)


pesos_total = str((dolares1 *valor_dolar)/1)

print("Tienes  $ "+ pesos_total + " pesos")
