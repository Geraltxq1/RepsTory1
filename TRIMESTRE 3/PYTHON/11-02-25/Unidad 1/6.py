print("Ejercicio nmero6")
ventas = []
print("Registro de ventas (ingrese 0 para terminar)")
producto = input("Ingrese el producto: ")

while producto != "0":
    valor = float(input("Ingrese el valor de la venta: "))
    
    if valor == 0:
        break
    
    ventas.append(valor)
    
    producto = input("Ingrese el producto: ")

if len(ventas) > 0:
    total = sum(ventas)
    cantidad = len(ventas)
    mayor = max(ventas)

    print("Resultados:")
    print("Total de ventas:", total)
    print("Cantidad de ventas:", cantidad)
    print("Venta más alta:", mayor)


