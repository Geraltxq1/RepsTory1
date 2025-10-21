## Imprime los numeros del 1 al 10 
for i in range (1, 11):
    print(i)

## Imprime los numeros del 5 al 20 de tres en tres 
for x in range (100, 200):
    print(x)

## Imprime los numeros del    
for j in range (5,21,3):
    print(j)
    
## Requerir al usuario que ingrese un numero 
## Entero positivo y luego imprimir todos los numeros 
# Desde 1 hasta ese Numero 
num = int(input("in(grese un numero entero positivo: "))
for k in range (1, num+ 1 ):
    print(k)
    
#Escribir al usuariio donde solicite una cantidad 
#y luego itere la cantidad de veces daadas. en cada interacion 
#Solicitar al usuario que ingrese Un numero. Al finalizar,
#mostar la suma de todos los numeros ingresados 

cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))
suma = 0
for i in range(cantidad):
    numero = int(input("Ingrese un numero: "))
    suma += numero 
print("La suma de los numeros ingresados es:",suma)

#Solicitar al usuario que ingrese una frase y luego imprimir 
#un listado de las volales que aparecen en esa frase(Sin Repetirlas)
frase = input ("Ingrese una Frase: ")
for x in "aeiou":
    if x in frase:
        print(x)
        
### contar la cantidad de vocales en una frase ingresada por el usuario

frase2 = input("Ingrese una Frase: ")
cantidad = 0 
for i in "aeiou":
    cantidad += 1
print ("La cantidad de vocacles en la frasse es", cantidad)

