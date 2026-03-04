import database

from datetime import datetime


# ===============================
# REGISTRAR
# ===============================

def registrar_venta():

    cliente = input("Nombre cliente: ").strip()

    tipo = input("Tipo cliente (normal/premium): ").strip()

    try:

        monto = float(input("Monto: "))

    except:

        print("Error, debe ingresar número")

        return

    fecha = datetime.now()

    database.insertar_venta(cliente, tipo, monto, fecha)

    print("Venta registrada correctamente")


# ===============================
# MOSTRAR
# ===============================

def mostrar_ventas():

    ventas = database.obtener_ventas()

    print("\n--- LISTADO ---")

    for v in ventas:

        print(

            "ID:", v[0],

            "| Cliente:", v[1],

            "| Tipo:", v[2],

            "| Monto:", v[3],

            "| Fecha:", v[4]

        )


# ===============================
# ACTUALIZAR
# ===============================

def actualizar():

    try:

        id = int(input("ID venta: "))

        monto = float(input("Nuevo monto: "))

    except:

        print("Error")

        return

    database.actualizar_venta(id, monto)

    print("Actualizado")


# ===============================
# ELIMINAR
# ===============================

def eliminar():

    try:

        id = int(input("ID venta: "))

    except:

        print("Error")

        return

    database.eliminar_venta(id)

    print("Eliminado")


# ===============================
# MENÚ
# ===============================

def main():

    database.crear_tabla()

    while True:

        print("\n--- SISTEMA DE VENTAS MYSQL ---")

        print("1 Registrar venta")

        print("2 Mostrar ventas")

        print("3 Actualizar venta")

        print("4 Eliminar venta")

        print("5 Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":

            registrar_venta()

        elif opcion == "2":

            mostrar_ventas()

        elif opcion == "3":

            actualizar()

        elif opcion == "4":

            eliminar()

        elif opcion == "5":

            print("Adiós")

            break

        else:

            print("Opción inválida")


# ===============================

if __name__ == "__main__":

    main()
