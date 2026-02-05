total_ventas_dia = 0 
clientes = 0 
afiliados = 0 
altas = 0 
nombre = input("Cliente: ") 
total_compra = 0
total_final = 0 

while nombre != 0 :
    tipo = input("Tipo (regular/afiliado): ") 
    edad = int(input("Edad: "))   
    producto = input("Producto (0 para terminar): ") 
    
    while producto != 0: 
        precio = int(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        total_compra = precio + cantidad
        producto = input("Producto (0 para terminar): ") 
        descuento = 0 
        if tipo == "afiliado": 
            descuento = descuento + 0.10 
            afiliados = afiliados + 1 
        if edad >= 60: 
            descuento = descuento + 0.05
            total_final = total_compra - descuento 
        if total_final > 500000:
            print("Compra alta") 
            altas += 1 
            total_ventas_dia = total_ventas_dia + total_final 
            clientes = clientes + 1 
        
        print("Total clientes: ", clientes) 
        print("Total ventas: ", + total_ventas_dia) 
        print("Afiliados:", afiliados) 
        print("Compras altas:", altas)
        
