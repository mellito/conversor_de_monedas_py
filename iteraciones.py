#WHILE
def main():
    # contador = 0
    # while contador < 10:
    #     print(contador)
    #     contador += 1 # esto es igual que contador = contador +1
    
    # contador_externo = 0
    # contador_interno = 0

    # while contador_externo < 5:
    #     while contador_interno <6:
    #         print(contador_externo, contador_interno)
    #         contador_interno +=1
    #     contador_externo +=1
    #     contador_interno=0
    x = 0.0
    for i in range(10):
        x += 0.1

    if x == 1.0:
        print(f'x = {x}')
    else:
        print(f'x != {x}')

if __name__ == '__main__':
    main()
