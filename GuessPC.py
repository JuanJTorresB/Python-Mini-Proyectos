import random
def Incio(Numero_Max, Numer_Min):
    Num_Random = random.randint(Numer_Min,Numero_Max)
    print(f"\n¿Tu numero es: {Num_Random}?")
    Desicion = str(input("¿Tu numero es Mayor (MA), Menor (ME) o he Acertado (A)"))
    Desicion = Desicion.upper()
    if Desicion == "MA":
        Numer_Min = Num_Random
        Incio(Numero_Max, Numer_Min+1)
    elif Desicion == "ME":
        Numero_Max = Num_Random
        Incio(Numero_Max-1, Numer_Min)
    elif Desicion == "A":
        print("He acertado, buen juego :3")
    else:
        print("Error Opcion No valida")
        Incio()
        

def guess_Pc(x):
    print(f"\nPiensa un numero de 0 a {x}")
    print("La computadora intentara adivinar tu numero ")
    print("Cuando la computadora haga su intento podras decir si es el numeor que estas pensando es Mayor(MA) Menor(ME) o si la computadora a Acertado (A)\n")
    choise = str(input("""¿Entendido?
    (S) Si (N) No\n"""))
    choise = choise.lower()
    if choise == "s":
        Numero_Max = x
        Numer_Min = 0
        Incio(Numero_Max ,Numer_Min)

    elif choise == "n":
        print("Otra vez :3")
        guess_Pc(10)
    else:
        print("Valor Invalido")
        guess_Pc(10)
    
guess_Pc(10)
print("\nGracias por usar nuestro programa <3")