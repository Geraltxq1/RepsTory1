# Ejercicio 1 
mi_dic = {"nombre ": "Karen", "Apellido": "Solis", "Edad": "35", "Ocupacion": "periodista"}
print(type(mi_dic))
print(mi_dic)

# Ejercicio 2 
mi_dic = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10, 300,15]}}

print(mi_dic["puntos"]["points2"][1])

# Ejercicio 3 
mi_dic = {"nombre ": "Karen", "Apellido": "Solis", "Edad": "35", "Ocupacion": "periodista"}
print(type(mi_dic))
mi_dic["Edad"]= "36"
mi_dic["Ocupacion"] = "Editora"
mi_dic["Pais"] = "Colombia"
print (mi_dic)

# Ejercicio 4 
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

print(int(mi_tupla.count(1)))
print(int(mi_tupla.count(2)))
print(int(mi_tupla.count(3)))

# Ejercicio 5 
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = mi_tupla 
print(mi_lista)

#Ejercicio 6 
mi_tupla = (1, 2, 3, 4)

a,b,c,d = mi_tupla
print(a)
print(b)
print(c)
print(len(mi_tupla))

# Ejercicio 7 

A1 = int(input("Ingrese numeros: "))
B2 = int(input("Ingrese numeros: "))
C3 = int(input("Ingrese numeros: "))
D4 = int(input("Ingrese numeros: "))
E5 = int(input("Ingrese numeros: "))

lista = (A1,B2,C3,D4,E5)

print("lista inversa")
for elemento in reversed(lista):
    print(elemento)