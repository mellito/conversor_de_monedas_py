# def imprimir_mensaje():
#     print("mensaje especial:")
#     print("Estoy aprendiendo a usar funciones")


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversaion(mensaje):
    print("Hola")
    print("como estas")
    print("elegiste la opcion " + mensaje)
    print("adios")

opcion = input("elige una opcion (1, 2, 3)")

if opcion == "1":
    conversaion(opcion)
elif opcion == "2":
    conversaion(opcion)
elif opcion == "3":
    conversaion(opcion)
else:
    print("escribe la opcion correcta")