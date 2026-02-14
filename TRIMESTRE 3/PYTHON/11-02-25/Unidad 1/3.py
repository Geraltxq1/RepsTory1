print("Ejercicio nmr3")

producto = input("Ingrese el producto a comprar: ")
costo_ini = int(input("Ingrese el valor o costo del producto: "))



if costo_ini >=200:
    descuento = costo_ini * 0.15
    descuento = costo_ini - descuento
elif costo_ini >= 100:
    descuento = costo_ini * 0.15
    descuento = costo_ini - descuento
else:
    descuento = 0

print("------------|------------------|-------------|---------------")
print("Informacion de venta: ")
print("Producto: ", producto)
print("Costo del Producto: ", costo_ini)
print("Descuento aplicado: ", descuento)


