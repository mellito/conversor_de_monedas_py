# contador = 0
# print("2 elevado a "+ str(contador) + " es igual a: " + str(2**contador))

def main():
    LIMITE = 100000
    contador= 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a "+ str(contador) + " es igual a: " + str(potencia_2))
        contador = contador+1
        potencia_2 = 2**contador    



# main
if __name__ == "__main__":
    main()