print("Ejercicio nmero8")

def calcular_descuento(monto, tipo_cliente):
    if tipo_cliente == "premium":
        return monto * 0.8   
    else:
        return monto       


monto = float(input("Ingrese el monto de la compra: "))
tipo = input("Tipo de cliente (normal/premium): ").lower()

total_final = calcular_descuento(monto, tipo)

print("Total a pagar:", total_final)
