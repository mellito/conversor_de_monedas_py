# menu = """"
# Bienvenido al conversor de monedas 😊

# 1 - Pesos colombianos
# 2 - Pesos argentinos
# 3 - Pesos mexicanos

# Elige una opcion: """

# opcion = input(menu)

# if opcion == "1":

#     pesos = input("cuantos pesos colombianos tienes? : ")
#     pesos = float(pesos)

#     valor_dolar= 4000
#     dolares = pesos/valor_dolar     
#     dolares = str(dolares)
#     print("Tienes  $ "+ dolares + " dolares")

# elif opcion == "2":  
#     pesos = input("cuantos pesos argentinos tienes? : ")
#     pesos = float(pesos)

#     valor_dolar= 65

#     dolares = pesos/valor_dolar     
#     dolares = str(dolares)
#     print("Tienes  $ "+ dolares + " dolares")

# elif opcion == "3":
#     pesos = input("cuantos pesos mexicanos tienes? : ")
#     pesos = float(pesos)

#     valor_dolar= 24



#     dolares = pesos/valor_dolar     
#     dolares = str(dolares)

#     print("Tienes  $ "+ dolares + " dolares")

# else:
#    print("opcion no valida")


#       codigo antiguo sin funciones

def conversor(tipo_pesos, valor_dolar):
     pesos = input("cuantos pesos "+ tipo_pesos +" tienes? : ")
     pesos = float(pesos)
     dolares = pesos/valor_dolar     
     dolares = str(dolares)
     print("Tienes  $ "+ dolares + " dolares")


menu = """"
# Bienvenido al conversor de monedas 😊

# 1 - Pesos colombianos
# 2 - Pesos argentinos
# 3 - Pesos mexicanos

# Elige una opcion: """

opcion = input(menu)

if opcion == "1":
    conversor("colombianos", 3875)


elif opcion == "2":  
    conversor("argentinos", 65)

elif opcion == "3":
    conversor("mexicanos", 24)

else:
   print("opcion no valida")

