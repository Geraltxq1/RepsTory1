#1 EJERCICIO 1 varlores_Cuadrado
valores = (5, 8, 9, 12, 36, 9.5)
valores_cuadrado = [v**2 for v in valores]
print(valores_cuadrado)

# EJERCICIO 2 Lista con los valores_pares
valores = (5, 8, 9, 12, 36, 9.5, 10)
valores_pares = [v for v in valores if v % 2 == 0]
print(valores_pares)  

#EJERCICIO 3 Conversión de Fahrenheit a Celsius
temp_fahrenheit = [32, 212, 275]
grados_celsius = [(f - 32) * (5/9) for f in temp_fahrenheit]
print("La conversion de grados a farenheit es:", grados_celsius)

# EJERCICIO 4 Unión de sets
set1 = {1, 2, "tres", "cuatro"}
set2 = {"tres", 4, 5}
set_3 = set1.union(set2)
print("UNion de set: ", set_3)

# EJERCICIO 5 Eliminar un elemento al azar de un set
import random
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
eliminado = sorteo.pop()    
print(f"Nombre eliminado del sorteo: {eliminado}")
print("lista con el nombre eliminado es: ", sorteo)

# EJERCICIO 6 Agregar un nombre al set
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damian")
print("Nombre añadido es: Damian")
print("Con el elemnto añadido es:", sorteo)

# EJERCICIO 7 Comparación que devuelve un booleano
prueba = 10 > 3
print("10 es mayor que 3? :", prueba)

# EJERCICIO 8 Verificar si 17834/34 es mayor que 87*56
resultado = (17834 / 34) > (87 * 56)
print("el resultado resulta:",resultado)

# EJERCICIO 9 Verificar si la raíz cuadrada de 25 es igual a 5
import math
resultado = math.sqrt(25) == 5
print("Raiz cuadrada de 25 es igual a 5?", resultado)

#======================================================

# Ejercicio 10 - Qué método debo usar para hallar el quinto carácter dentro del string
# “éxito”, almacenada en la variable palabra? 

# RESPUESTA: palabra [4]
#========================================================

# EJERCICIO 11 - Los booleanos pueden asumir los siguientes valores:

# RESPUESTA : TRUE Y FALSE
#=============================================================

# EJERCICIO 12 - Cuál de los siguientes objetos no serían admitidos por un set?Listas _
#string__ tuplas__ float__ integers__

#RESPUESTA: Listas