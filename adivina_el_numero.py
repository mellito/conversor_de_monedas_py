import random 

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido =int(input("Elige un numero del uno al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Intenta con un numero mas grande")
            
        else:
            print("Intenta con un numero mas pequeno") 
        numero_elegido = int(input("Elige otro numero: ")) 
    print("ganaste!")    


if __name__ =="__main__":
    run()