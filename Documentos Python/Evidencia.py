### Parte 1 Taller de Listas 
### Parte 2 Taller de Python

#Taller 1 Python Listas

#### lista con 5 elementos
mi_lista = ["texto", 893, "Python", "Hola", False , True ]
print(mi_lista)

#### "motocicleta"
vehiculo = ["avión", "auto", "barco", "bicicleta"]
vehiculo.append("motocicleta")
print(vehiculo)

#### Quitar el tercer elemento 
frutas = ["Manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2) 
print("Elemento eliminado:", eliminado)
print("Lista actualizada:", frutas)

#### Crear lista_numeros y mostrar el valor 90
lista_numeros = [10, 46, 78, 90, 102, 104]
print(lista_numeros[3]) 

#### Ordenar de mayor a menor
lista_numeros = [10, 45, 356, 16, 25, 18, 46, 67, 49, 98, 106, 43, 120, 65, 80]

lista_numeros.sort(reverse=True)
print("Lista ordenada de mayor a menor:", lista_numeros)




#Taller Python Parte 2
""""""""
print("Vamos a calcular el perimetro y area de un rectangulo")
base = int(input("Ingrese la Base de el Rectangulo: "))
altura = int(input("Ingrese la Altura de el Rectangulo: "))

perimetro = 2*base + 2*altura
area = base * altura

print("El perimetro de el rectangulo es:",perimetro)
print("El Area de el rectangulo es:",area)

""""""""""""""""""

print("Calcular la Media de 3 Numeros")
num1 = int(input("Ingrese un Numero "))
num2 = int(input("Ingrese un Numero "))
num3 = int(input("Ingrese un Numero "))

Promedio = (num1 + num2 + num3) / 3

print("El promedio de los numeros es:",Promedio)

""""""""""""""""""

print("Calcular nota de un Alumno")
Not1 = float(input("Calificacion 1: "))
Not2 = float(input("Calificacion 2: "))
Not3 = float(input("Calificacion 3: "))
exam_final = float(input("Calificación del examen final: "))
trabajo_fin = float(input("Calificación del trabajo final: "))

promedio_parciales = (Not1 + Not2 + Not3) / 3
calificacion_fin = (promedio_parciales * 0.55) + (exam_final * 0.30) + (trabajo_fin * 0.15)

print(f"La calificación final es: {calificacion_fin}")


""""""""""""

print("Precios De Entrada")
edad = int(input("Ingresa tu edad: "))

if edad >= 60:
    precio = 12000
elif edad <= 12:
    precio = 10000
else:
    precio = 15000

print(f"El precio de tu entrada es: {precio}")

""""""""
Lado_A = float(input("Lado A: "))
Lado_B = float(input("Lado B: "))
Lado_C = float(input("Lado C: "))

if Lado_A == Lado_B == Lado_C:
    print("El triángulo es equilátero")
elif Lado_A ==  Lado_B or Lado_A == Lado_C or Lado_B == Lado_C:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
    
""""""""
print("Pedir Nombre")
nombre = input("¿Cuál es tu nombre?: ")
print(f"¡Hola {nombre}!")

""""""""

nm1 = int(input("Ingresa el primer número: "))
nm2 = int(input("Ingresa el segundo número: "))

suma = 0
for i in range(nm1, nm2 + 1):
    suma += i

print(f"La suma de los enteros entre {nm1} y {nm2} es: {suma}")
