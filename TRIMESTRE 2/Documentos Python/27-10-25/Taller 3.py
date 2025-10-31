# Utilizando loops For, saluda a todos los miembros de una clase,
# imprimiendo "Hola" + su nombre.
# Por ejemplo: "Hola María"
# alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel",
# "Tomás", "Daniela"]

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for letra in alumnos_clase: 
    print(f"Hola Como estas?, {letra}")
    
# Dada la siguiente lista de números, realiza la suma de todos los
# números utilizando loops For y almacena el resultado de la suma en
# una variable llamada suma_numeros:
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma = 0

for num1 in lista_numeros:
    suma += num1
    print("La suma de los numeros es:",suma)

# Dada la siguiente lista de números, realiza la suma de todos los
# números pares e impares* por separado en las variables suma_pares
# y suma_impares respectivamente:
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# Recordando que: el módulo (o resto) de un número dividido 2 es cero
# cuando dicho valor es par, y 1 cuando es impar
# num % 2 == 0 (valores pares)
# num % 2 == 1 (valores impares)

lista_valores = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0 
suma_impares = 0 

for numb in lista_valores:
    if numb % 2 == 0:
        suma_pares += numb
    else:
        suma_impares += numb
    
print("La suma de los numeros impares es: ", suma_impares)
print("La suma de los numeros pares es: ", suma_pares)

# Crea un Loop While que se imprima en pantalla los números del 10 al
# 0, uno a la vez.

contador = 10
while contador >= 0:
        print("numero", contador)
        contador -= 1

# Crea una lista formada por todos los números desde el 2500 al 2585
# (inclusive). Almacena dicha lista en la variable mi_lista.
my_lista = []
for lista in range (2500, 2586):
    my_lista.append(lista)
print(my_lista)

# Utilizando la función range(), crea en una única linea de código una
# lista formada por todos los números múltiplos de 3 desde el 3 al 300
# (inclusive). Almacena dicha lista en la variable mi_lista.

lista_numeros = list(range(3, 301, 3))

# Utiliza la función range() y un loop para sumar los cuadrados de todos
# los números del 1 al 15 (inclusive). Almacena el resultado en una
# variable llamada suma_cuadrados.
# Para ello:
# • Crea un rango de valores que puedas recorrer en un loop
# • Para cada uno de estos valores, calcula su valor al cuadrado
# (potencia de 2). Puede que necesites crear variables intermedias
# (de manera opcional).
# • Suma todos los valores al cuadrado obtenidos. Acumula la suma
# en la variable suma_cuadrados.


suma_cuadrados = 0
for numeros in range (1,16):
    cuadrado = numeros ** 2
    suma_cuadrados += cuadrado
print(suma_cuadrados)

# Imprime en pantalla frases como la siguiente:
# '{nombre} se encuentra en el índice {indice}'.
# Donde nombre debe ser cada uno de los nombres de la lista a
# continuación, y el índice, obtenido mediante enumerate().
# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]
# Puedes modificar la línea print() otorgada como ejemplo, pero las
# frases entregadas deberán ser iguales.
# Tip: utiliza loops! 

print("Obtenemos indice y valor con enumerate: ")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]
for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre}, esta en el indice:{indice}")

# Crea una lista formada por las tuplas (indice, elemento), formadas a
# partir de obtener mediante enumerate() los índices de cada caracter del
# string "Python".
# Llama a la lista obtenida con el nombre de variable lista_indices.

lista_indice = list(enumerate("python"))
print(lista_indice)

# Imprime en pantalla únicamente los índices de aquellos
# nombres de la lista a continuación, que empiecen con M:
# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]
# Puedes resolverlo de diferentes maneras, pero servirá que tengas
# presente todos o algunos de los siguientes elementos:
# • Loops
# • Condicionales if
# • El método enumerate()
# • Métodos de strings o indexado

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)