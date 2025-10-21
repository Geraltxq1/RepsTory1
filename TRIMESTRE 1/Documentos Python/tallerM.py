# Ejercicio: 1
palabra = "ordenador"
print(palabra[4])  

#Ejercicio: 2
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.find("práctica"))   

#Ejercicio: 3
print(frase.rfind("práctica"))  

#Ejercicio: 4
frase2 = "Controlar la complejidad es la esencia de la programación"
print(frase2[:9])   

#Ejercicio: 5
frase3 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase3[8::3])

#Ejercicio: 6
frase4 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase4[::-1])

#Ejercicio: 7
print(874 // 27)

#Ejercicio: 8
print(456 % 33)

#Ejercicio: 9
import math
print(math.sqrt(783))

#Ejercicio: 10
print(round(10/3, 2))

#Ejercicio: 11
print(round(10.676767))

#Ejercicio: 12
print(round(math.sqrt(5), 4))

#Ejercicio: 13
nombre = input("Ingrese el nombre")
venta = float(input("Ingrese valor de la venta del mes: "))
comision = venta * 0.13
print(f"El vendedor {nombre} tiene una comisión de: {comision}")

#Ejercicio: 14
texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(texto.upper())

#Ejercicio: 15
lista_palabras = ["La", "legibilidad", "cuenta."]
print(" ".join(lista_palabras))

# 16
frase5 = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase5 = frase5.replace("difícil", "fácil").replace("mala", "buena")
print(frase5)
