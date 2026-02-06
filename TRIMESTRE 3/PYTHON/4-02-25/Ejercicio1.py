
total_ventas_dia = 0
clientes = 0
afiliados = 0
altas = 0
print("-----------|-------------|-------------|-------------------")
print("👧ANA")
print("Total Compra: 300.000")
print("Descuento Total: 15% 45.000")
print("Total Final: 255.000")
print("Alto Valor: No Aplica")
print("-----------|-------------|-------------|-------------------")
print("🧒Luis")
print("Total Compra: 80.000")
print("Descuento Total: No Aplica")
print("Total Final: 80.000")
print("Alto Valor: No Aplica")
print("-----------|-------------|-------------|-------------------")


nombre = input("🧒Cliente (FIN para terminar): ")

while nombre != "FIN":
    tipo = input("Tipo (regular/afiliado): ")
    edad = int(input("Edad: "))
    print("--------------------------------------------------------")


    total_compra = 0 # para q se reicnie por cliente 
    producto = input("Ingrese el Producto (0 para terminar): ")
    
    while producto != "0":
        precio = float(input("Precio: "))
        while precio < 0:
            print("La cantidad debe ser positiva")
            precio = float(input("Precio: "))

        cantidad = int(input("Cantidad: "))
        while cantidad < 0:
            print("La cantidad debe ser positiva")
            cantidad = int(input("Cantidad: "))

        print("--------------------------------------------------------")
        total_compra = total_compra + precio * cantidad
        producto = input("Producto (0 para terminar): ")

    descuento = 0

    if tipo == "afiliado":
        descuento = descuento + 0.10
        afiliados = afiliados + 1

    if edad >= 60:
        descuento = descuento + 0.05

    total_final = total_compra * (1 - descuento)

    if total_final > 500000:
        print("Compra alta!!!✅")
        print("--------------------------------------------------------")

        altas += 1

    total_ventas_dia = total_ventas_dia + total_final
    clientes = clientes + 1

    nombre = input("Cliente (FIN para terminar): ")

print("Total clientes:", clientes)
print("Total ventas:", total_ventas_dia)
print("Afiliados:", afiliados)
print("Compras altas:", altas)


