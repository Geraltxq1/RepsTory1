import random

def generar_numero():
    
    return random.randint(1, 100)
def pedir_numero():
    while True:
        try:
            numero = int(input("Ingresa un número entre 1 y 100: "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("Nuevo invalido, ingrese otro")
        except ValueError:
            print("Numero no valido")

def verificar_intento(numero_secreto, intento):
    if intento < numero_secreto:
        print("Numero bajo, Intenta con un número mas alto")
        return False
    elif intento > numero_secreto:
        print("Numero alto, Intenta con un número mas bajo")
        return False
    else:
        print("Felicidades adivinaste el número ")
        return True

def jugar():
    print("=== Bienvenido al juego de Adivina el Número ===")
    numero_secreto = generar_numero()
    intentos = 0

    while True:
        intento = pedir_numero()
        intentos += 1
        if verificar_intento(numero_secreto, intento):
            print(f"Lo lograste en {intentos} intentos.")
            break
jugar()
