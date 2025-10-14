mi_lista= ["Juan", "Pablo", "David", "Felipe", "Pedro"] # Imprime una lista
print(mi_lista)

print("="*60)

medios_transporte= ["Avion", "Auto", "Barco", "Bicicleta"] #Agrega caracter sin modificar la linea
medios_transporte.append("motocicleta")
print(medios_transporte)

print("="*60)

frutas= ["manzana","banano","mango","cereza","sandia"] #Elimina un caracter sin modificar la linea
eliminado= frutas.pop(3)
print(frutas)
print(eliminado)


print("="*60)

lista_numeros= [10,46,78,90,102,104] # Imprime un numero especifico, desde el cero
print(lista_numeros[3])

print("="*60)

lista_numeros= [10,45,356,16,25,18,46,67,49,98,106,43,120,65,80]
lista_numeros.sort(reverse=True) #Con Reverse true de mayor a menor - Quitar para cambiar
print(lista_numeros)