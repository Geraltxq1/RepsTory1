print("Ejercicio nmero7")
cliente = {
    "nombre": input("Ingrese el nombre del cliente: "),
    "tipo": input("Tipo de cliente (normal/premium): ").lower(),
    "activo": True
}

if cliente["tipo"] == "premium":
    print("Cliente con beneficios especiales ")
else:
    print("Cliente estándar")
