print("Ejercicio nmero9")
def registrar_ventas():
    ventas = []
    print("Registro de ventas (ingrese 0 para terminar)")
    
    while True:
        valor = float(input("Ingrese el valor de una venta: "))
        if valor == 0:
            break
        ventas.append(valor)
    
    return ventas


def total_ventas(ventas):
    return sum(ventas)


def promedio_ventas(ventas):
    return sum(ventas) / len(ventas)

def contar_mayores_100(ventas):
    contador = 0
    for v in ventas:
        if v >= 100:
            contador += 1
    return contador

def contar_menores_100(ventas):
    contador = 0
    for v in ventas:
        if v < 100:
            contador += 1
    return contador

ventas = registrar_ventas()

if len(ventas) > 0:
    print("Resultados:")
    print("Total de ventas:", total_ventas(ventas))
    print("Promedio de ventas:", promedio_ventas(ventas))
    print("Ventas mayores a 100:", contar_mayores_100(ventas))
    print("Ventas menores a 100:", contar_menores_100(ventas))
else:
    print("No hya ventas registradas")
