import random 

def guess(x):
    random_number = random.randint(1, x) #Numero random Entero entre 1 y x
    guess = 0 #Declaramos la variable para poder usarla en el loop pero con un valor que asegure el inicio por  lo menos 1 vez
    while guess != random_number: #Mientras no adivinemos el numero el loop continuara
        guess = int(input(f"Intenta Advinar el Numero entre 1 y {x} :"))
        if guess < random_number:
            print("")
            print("El numero es Mayor Jijiji <3")
            print(" ")
        elif guess > random_number:
            print(" ")
            print("El numero es Menor Jijiji <3")
            print(" ")
        else:
            print(" ")
            print(f"Has acertado, el Numero era {random_number} Felicidades <3")
            print(" ")
        
guess(10)