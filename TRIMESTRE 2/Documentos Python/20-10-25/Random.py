from random import *

# Recorremos los numeros del 20 al 40 inclute al 20 y 40
print(" Numeros del 20 al 40")
for numero in range(20, 41 ):
    print(numero)
    
#=======================

# Crear una lista de numeros del 30 al 50 con paso 2 
print("Lista de Numeros = list(30, 51, 2 )")
lista_numeros = list(range(30, 51, 2)) # paso de 2 
print(lista_numeros)

#===================

#Enumerate : permite obtener el indice y valor 
# de cada elemento en una lista o iterable 

print("Usando enumerayte para obtener indice y valor")
lista = [ "a", "b", "c", "d"]
for indice, valor in enumerate(lista):
    print(f"indice: {indice}, valor: {valor}")
    
#=================================

print("Ejemplo os de enumerate ")
lista1 = ["a", "b", "c", "d", "e"]
for item in enumerate(lista1):
    print(item)
    
#==============================================
# Guardar en una tupla la lista cin indice y valor 
lista2 = [ "x", "y", "z"]
tupla_enumerada = tuple(enumerate(lista2))
print("Tupla con indice y valor", tupla_enumerada)

#
usando zip para combianr dos listas 

lista_nombres = ["ana"]
lista_edades = [25,30, 22]
lista_ciudades = ["Madrid", "Barcelona", "valencia"]

#Emparejar las listas usando Zip
combinado = lista(zip(lista_nombres, lista_edades, lista_ciudades))
# Recorrer cada tupka en lista combinada
for nombre, edad, ciudad in combinado:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad : {ciudad}")

#main()  - Max()  devuelven el minimo y el maximo de un iterable 
#o menor o mayor entre varios argumentos 
menor = min(78,56,89,23,45)
mayor = max(78,56,89,23,45)
print (f"el menor es: {menor}")
print (f"el mayor es: {mayor}")
#=====================
lista = [12,45,7,23,89,34]
print(max(lista)) # Maximo en la lista
print(min(lista)) # Minimo en la lista

#min ouede funcionar con cadenas; usa orden alfabetico

nombre = ["ana","Luis", "Carlos", "Beatriz"]
print("Nombre mneor alfabeticamente:", min(nombre))
print("Nombre Mayor alfabeticamente:", max(nombre))

# En cadenas, min( y max () usan el valor ASCII
cadena = "Python"
print("Caracter minimo en 'Python': ", min(cadena)) # h 
print("Caracter minimo en 'Python': ", max(cadena)) # Y 

#========================
nom = "Alejandra"
print("Caracter minimo en alejandra:", min(nom))
# 'a' letras mas pequeñas
print("Caracter maxio en alejandra: ", max(nom))
# 'r' letra mas grande

#==============================0
# En diccionario, min() y max( trabajan con las Claves)
diccionario = {'a': 5, 'b': 2, 'c': 8}
print("Caleve minima en diccionario:", min(diccionario) ) # 'a'
print("Caleve maximo en diccionario:", max(diccionario) ) # 'c'
print(min(diccionario.values())) # Valor minimo 2 
print(max(diccionario.values())) # Valor maximo 8

#Funciones de Ramdom 
# randit (a,b) devuelve un numero entero aleatroio entre a y b 
# Inclusive
num_aletariotio = randint(1,100)
print("Numero aleatorio entre 1 y 100", num_aletariotio)

#==========================
#Uniform(a,b) Devuelve un numero Flotante - DEcimal
#aleatorio entre a y b 
aleatorio_flotante = uniform(1.0, 10.0)
print("Numero flotante aleatorio entre 1.0 y 10.0:", aleatorio_flotante)

#======================
#randim( devuelve un numero flotante aleatorio entre 0.0 y 1.0 
aleatorio_0_1 = random()
print("Numero aleatorio entre 0.0 y 1.0", aleatorio_0_1)

#========================0
#Choice(iterable) selecciona un elemento aleatorio de un iterable
colores = ["rojo", "azul", "verde", "amarillo"]
color_seleccionado = choice(colores)
print(" Color Seleccionado aleatoriamente:", color_seleccionado)

#Shuffle(lista) MEzcla los elementos de una lista 
numeros = [1,2,3,4,5]
print("Lista original de numeros", numeros)
shuffle(numeros)
