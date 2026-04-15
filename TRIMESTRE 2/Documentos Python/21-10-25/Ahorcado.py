import random

def elegir_palabra():

    palabras = ["julian", "andres", "juanes", "edu", "juanma", "sebastian", "silvana", "gaitan"]
    return random.choice(palabras)



def mtr_pgrso(palabra_secreta, letras_correctas):
    progreso = ""
    for letra in palabra_secreta:
        if letra in letras_correctas:
            progreso += letra + " "
        else:
            progreso += "_"
    return progreso.strip()


def ltra():
    while True:
        letra = input("Elige una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("ingresa solo una letra validaa: ")
        else:
            return letra
        
        
def gndr(palabra_secreta, letras_correctas):
    for letra in palabra_secreta:
        if letra not in letras_correctas:
            return False
    return True


def jgr_ardo():
    print("Juego de Ahorcado")
    print("_"*20)
    palabra = elegir_palabra()
    vidas = 6
    letras_correctas = []
    letras_incorrectas = []
    print(f"\nLa palabra secreta tiene {len(palabra)} letras")
    
    
    while vidas > 0:
        print(f"\nVidas restantes: {vidas}")
        
        print("Palabra:", mtr_pgrso(palabra, letras_correctas))
        print("Letras incorrectas:", ", ".join(letras_incorrectas))

        letra = ltra()

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya has ingresado esta letra")
            continue

        if letra in palabra:
            print("La letra esta en la palabra")
            letras_correctas.append(letra)
        else:
            print("Esa letra no esta en la palabra")
            letras_incorrectas.append(letra)
            vidas -= 1

        if gndr(palabra, letras_correctas):
            print("\nFeliciades! adivinaste la palabra, Completaste el ahorcadp:", palabra)
            break
    else:
        print("\nTe quedaste sin vidas, La palabra era:", palabra)


if __name__ == "__main__":
    jgr_ardo()
