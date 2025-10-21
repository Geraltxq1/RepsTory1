#
#
#
#
#
#
# Puedes generar una lista aplicando
# Una expresion a cada elemento iterable 
# como (lista, tupla o rango)

#===================
# forma tradicional de crear una lista a partir de un string 
palabra = "Python " # cadena Base
lista_tracicional = [] # Lista vacia 
for letra in palabra: #Bucle for para recorrer 
    lista_tracicional.append(letra)
    # Agregar letra ala Lista 
print("Lista Tradicional:", lista_tracicional)

# Misma idea unsado compresion de listas 
palabra =  "python"
lista_compresion = [letra for in palabra]
# Toma cada caracteer de palabara y la pone en una lista
print("Lista por compresion", lista_compresion)

#===================================
# Otra variante usando compresion de listas 
# El nombre de la variable interna puede ser diferente

lista1 = [ caracter for caracter in "Python"]
# Recorre directamente el strinf "Python "
print("Otra lista por compresion", lista1)

#====================================

#Compresion con numeros: 
# Crear una lista de pares de 0 a 20 
listanum = [n for n in range (0, 21, 2)]
print("Lista de numeros Pares:", listanum)


# Convertir pies a metros 
# 1 pie = 0.3048 metros 
pies = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
metros = [round(pie * 0.3048, 4 )for pie in pies]
print("Pies a Metros:",metros)

#==============================

# Conversion de temperaturas
# Convertir grados celcius a fahrenheit 
celsius = [0 , 10, 20 ]
farenheit = [round ((temp * 9/5)+ 32, 2 )for temp in celsius]
print("Celsius a farenheit:", farenheit)

#==================================

