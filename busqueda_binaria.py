def main():
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo: {bajo} Alto: {alto} Respuesta: {respuesta}')
        if respuesta**2 < objetivo:
            bajo=respuesta
        else:
            alto=respuesta

        respuesta =(alto+bajo)/2  

        print(f'la raiz cuadrada del {objetivo} es {respuesta}')  


if __name__ == '__main__':
    main()