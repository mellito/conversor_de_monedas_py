def main():
    objetivo = int(input('escoje un numero: '))
    epsilon= 0.0001
    paso = epsilon**2
    respuesta =0.01

    while abs(respuesta**2 - objetivo )>= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo ), respuesta)
        respuesta += paso


    if abs(respuesta **2 - objetivo) >= epsilon:
        print(f'no se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')



if __name__ == '__main__':
    main()