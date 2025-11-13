# Primer EJercicio
print("Hola mundo")
""""""
# Segundo EJercicio
nombre = input("Ingrese su nombre")
print("Tu nombre es ",nombre)
""""""
# Tercer Ejercicio
nm1 = int(input("Ingrese un numero: "))
nm2 = int(input("Ingrese un numero: "))

print("Tu numero es: ",nm1+ nm2)
""""""
# Cuarto EJercicio
print("Nuevo reto")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

SumaP = num1+ num2 + num3

promedio = SumaP / 3

print("El promedio de los 3 numeros es: ",promedio)
""""""

# 5
from datetime import datetime
Edad = int(input("Igrese su edad: "))
actual_Año = datetime.now().year
faltan = 100 - Edad
Año_100 = actual_Año + faltan
print(F"Tendras 100 años en el año {Año_100}")

""""""

# 6
num1 = int(input("Ingrese un Numero: "))
if num1 == 0/2:
    print("Tu numero es Par")
else:
    print("Tu numero es Impar")
""""""

# 7

Edad = int(input("Ingresa tu edad: "))
if Edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
""""""

# 8

nm1 = int(input("Ingresa un Numero: "))
nm2 = int(input("Ingresa un Numero: "))
nm3 = int(input("Ingresa un Numero: "))

mayor =max(nm1, nm2, nm3)
print("El numero mayor es:",mayor)
""""""

# 9

Numero_secreto = 10

Adivina = int(input("Adivina El Numero Secreto: "))

if Adivina == Numero_secreto :
    print("Has Encontrado el numero Secreto")
else:
    print("Has Fallado al Encontrar el Numero")

#10 


