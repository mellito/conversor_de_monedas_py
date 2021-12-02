# def main():
#     number1 =int(input("escoge tu primer numero: "))
#     number2 =int(input("escoge tu segundo numero: "))

#     if number1 > number2:
#         print("el primer numero es mayor que el segundo")
#     elif number1 < number2:
#         print("el segundo numero es mayor que el primero")
#     else:
#         print("los 2 numeros son iguales")

# if __name__ =="__main__":
#     main()

def main():
    name1= input("Hola jugador 1 podrias darme tu nombre porfavor: ")
    edad1= int(input(f'Hola {name1} y tu edad cual es: '))
    name2= input("Hola jugador 2 podrias darme tu nombre porfavor: ")
    edad2= int(input(f'Hola {name2} y tu edad cual es: '))

    if edad1 > edad2:
       print(f'{name1} es mayor que {name2}')
    elif edad1 < edad2:
         print(f'{name2} es mayor que {name1}')
    else:
         print(f'{name2} y {name1} tienen la misma edad')

if __name__=='__main__':
    main()