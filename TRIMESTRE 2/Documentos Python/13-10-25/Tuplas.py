# Las tuplas son colecciones ordenadas e inmutables 
# Es decir, una vez creadas no se pueden modificar 
# (no se pueden agregrar, eliminar o camnbiar elementos)
# Se definen usando parentesis ()
# Pueden contener elementos de direntes tipos de datos
# Son utiles para almacenar datos que no deben camnbiar
# Como cordenadas geograficas, fechas, etc 
# Para proteger datos de modificaciones accidentales 
# Caracteristicas 
# Ocupan menos espacio en memoria que las listas 
# Son mas rapidas que las listas para ciertas operaciones
# Pueden tener diferentes tipos de datos 
# Se pueden anidar 

# ejemplo basico de una tupla 
mi_tupla = (1,2,3,4)
print (type(mi_tupla))
print(len(mi_tupla))

# Ejemplo de tupla con diferentes tipos de datos 

mi_tupla1 = (1, "hola", 3.14, True)
print(type(mi_tupla1))
print(mi_tupla1)
tupla = (1,2,3,4,5)

print (tupla[0 ]) # Acceder al primer elemento
print (tupla[1:4]) # Acceder a una porcion de la tupla
print (tupla[-1]) #acceder al ultimo elemento

# Tuplas Anidadas 
tupla_anidada = (1,2,(3,4), (5,6))
print(tupla_anidada[2]) #acceder ala tupla (3,4)

# Intentar Modificar una tupla genera un error
# tupla2 = (1,2,3)
# tupla2[0] = 10 # Esto genera un error 
# print(tupla2)

#Operaciones con tuplas 
tupla1 = (1,2,3)
tupla2 = (4,5,6,)
tupla3 = tupla1 + tupla2 # Concatenacion 
print(tupla3)

print(tupla3)
print(tupla3.count (2)) #Contar cuantas veces aparece el valor
print(tupla3.index(5))  #Encontar la posicion del valor  5

#desempaquetado de tuplas 
tupla4 = ( 10, 20, 30 )
a, b, c = tupla4 

print (a) # 10 
print (b) # 20 
print (c) # 30 
print(len(tupla4))
#tuplas con un solo elemento

tupla5 = (100,) #  nota como al final 
print (type(tupla5)) # es una tupla 
print (tupla5[0]) # 100
#sin la coma seria un entero 

tupla6 = (100) # sin coma 

# metodos de tuplas 

t = (1,2,3,4,5,1) 
print(t.count(1)) #Cuantas veces aparece el 1
print(t.index(3)) # En que posicion esta el 3 
print(len(t)) # Longitud de la tupla 
print(3 in t) # Verficar si el 3 esta en la tupla


#iterar sobre una tupla 
tupla7 = ("a", "b", "c")
for elemento in tupla7:
    print(elemento)
    
    
#Repetir una tupla 
tupla8 = (1,2 )
tupla9 = tupla8 *3 
print(tupla9) # (1,2,1,2,1,2)

#convertir una lista en tupla 
mi_lista = [1,2,3]
mi_tupla = tuple(mi_lista)
print (mi_tupla) #(1,2,3)

#Comprobar si un elemento esta en la tupla 
tupla10 = (10,20,30)
if 30 in tupla10:
    print("30 esta en la tupla ")
else:
    print("30 no esta en la tupla ")
    
# crear una tupal con datos y mostralos formateado s
persona = ("juan",25, "manizales")

print(f"nombre {persona[0]}, Edad: {persona[1]}, Ciudad: {persona[2]}")

