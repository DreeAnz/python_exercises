import random
import time


deadpool_vida = int(input("Ingresa la vida de Deadpool: "))
wolverine_vida = int(input("Ingresa la vida de Wolverine: "))

turno = 0
regenerar = 0

while(deadpool_vida and wolverine_vida > 0):

    turno +=1
    print(f"\nTurno: {turno}")

    #Bloque de deadpool
    if(regenerar == 1):
        print("Deadpool se esta regenerando...")
        regenerar=0

    elif(random.random() > 0.2):

        ataque_deadpool = random.randint(10,100)
        print(f"Deadpool ataca con {ataque_deadpool}")


        if(ataque_deadpool == 100):
            print("Deadpool dio un golpe max. Wolverine no atacara en el siguiente turno.")
            regenerar=1

        wolverine_vida -=ataque_deadpool

        if(wolverine_vida <= 0):
            break
        else:
            print(f"Vida restante de Wolverine; {wolverine_vida}")
        
    else:
        print("¡Wolverine esquivo el ataque!")


    #Bloque de wolverine
    if(regenerar == 1):
        print("Wolverine se esta regenerando...")
        regenerar=0

    elif(random.random() > 0.25):

        ataque_wolverine = random.randint(10,120)
        print(f"Wolverine ataca con {ataque_wolverine}")

        if(ataque_wolverine == 120):
            print("Wolverine dio un golpe maximo. Deadpool no atacara en el siguiente turno.")
            regenerar=1

        deadpool_vida -= ataque_wolverine

        if(deadpool_vida <= 0):
            break
        else:
            print(f"Vida restante de Deadpool: {deadpool_vida}")

    else:
        print("¡Deadpool esquivo el ataque!")

    time.sleep(1)


if(deadpool_vida <= 0):
    print("\nMurio Wade... \nGana Wolverine")
else:
    print("\nMurio Logan... \nGana Deadpool")