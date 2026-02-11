print("Tienda")
Tipo_Usuario = input("normal/premium: ").lower()
producto = input("Que deseas Comprar?: ")
p_producto = int(input("Precio del Producto?: "))

total = 0
if Tipo_Usuario == "premium":
    descuento = p_producto * 0.20
    total = p_producto - descuento
    
elif Tipo_Usuario == "normal":
    if p_producto > 100:
        descuento = p_producto * 0.10
        total = p_producto - descuento
    else:
        print("No tienes descuento")
        total = p_producto
else:
    print("Tipo de usuario no válido")
    total = p_producto
    
print("El total a pagar es de", total)
