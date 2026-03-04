from datetime import datetime
tickets = []

AREAS_VALIDAS = ["TI", "Contabilidad", "Operaciones", "RRHH"]
PRIORIDADES_VALIDAS = ["baja", "media", "alta"]
ESTADOS_VALIDOS = ["abierto", "en proceso", "cerrado"]

def mostrar_menu():
    print("\n===== Sistema de Tickets =====")
    print("=" * 150)
    print("1. Registrar ticket")
    print("2. Cambiar estado de ticket")
    print("3. Generar reporte general")
    print("4. Listar todos los tickets")
    print("5. Salir")

def validar_area(area):
    return area in AREAS_VALIDAS

def validar_prioridad(prioridad):
    return prioridad in PRIORIDADES_VALIDAS

def registrar_ticket():
    try:
        usuario = input("Nombre del usuario: ").strip()            #.strip() Esto hace que no haya espeacios 
        area = input(f"Area {AREAS_VALIDAS}: ").strip().lower()         #.strip() Esto hace que no haya espeacios 
                                                                        #Lower() pasa de mayusculas a minusculas asi no hya errores
        descripcion = input("Descripcion del problema: ").strip()       #.strip() Esto hace que no haya espeacios 
        prioridad = input(f"Prioridad {PRIORIDADES_VALIDAS}: ").strip()    #.strip() Esto hace que no haya espeacios 

        if not descripcion:
            print("La descripcion no puede estar vacia")
            return

        if not validar_area(area):
            print(" Area invalida.")
            return

        if not validar_prioridad(prioridad):
            print("Prioridad invalida")
            return

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ticket = {
            "usuario": usuario,
            "area": area,
            "descripcion": descripcion,
            "prioridad": prioridad,
            "estado": "abierto",
            "fecha": fecha
        }

        tickets.append(ticket)  #append añade ticket ala lista

        print("Ticket registrado correctamente")

        if prioridad == "alta":
            print("Prioridad de Ticket ALTA")

    except Exception as e:
        print("Error al registrar ticket:", e)


def cambiar_estado():
    try:
        if not tickets:
            print("No hay tickets registrados")
            return

        listar_tickets()

        indice = int(input("Ingrese el numero del ticket: "))

        if indice < 0 or indice >= len(tickets):
            print("indice invalido")
            return

        nuevo_estado = input(f"Nuevo estado {ESTADOS_VALIDOS}: ").strip()

        if nuevo_estado not in ESTADOS_VALIDOS:
            print("Estado inválido")
            return

        tickets[indice]["estado"] = nuevo_estado
        print("Estado actualizado correctamente")

    except ValueError:
        print("Debe ingresar un número valido")
    except Exception as e:
        print("Error:", e)


def generar_reporte():
    print("\n===== REPORTE GENERAL =====")

    total = len(tickets)
    print("Total de tickets:", total)

    if total == 0:
        return

    altas = len([t for t in tickets if t["prioridad"] == "alta"])

    por_prioridad = {p: len([t for t in tickets if t["prioridad"] == p])
                    for p in PRIORIDADES_VALIDAS}

    por_estado = {e: len([t for t in tickets if t["estado"] == e])
                for e in ESTADOS_VALIDOS}

    por_area = {a: len([t for t in tickets if t["area"] == a])
                for a in AREAS_VALIDAS}

    print("Tickets por prioridad:", por_prioridad)
    print("Tickets por estado:", por_estado)
    print("Tickets por área:", por_area)
    print("Tickets prioridad alta:", altas)

    mas_reciente = max(tickets, key=lambda x: x["fecha"]) # Esto hace que se busque la fecha del ticket mas reciente o mas grande
    print("Ticket más reciente:", mas_reciente)           #lambda hace que se compare la fecha con el max 


def listar_tickets():
    if not tickets:
        print("No hay tickets registrados")
        return

    print("\n===== LISTADO DE TICKETS =====")
    for i, ticket in enumerate(tickets):            #enumerate Permite recorrer una lista y obtener su posicion de el 
        print(f"\nTicket #{i}")
        for clave, valor in ticket.items():
            print(f"{clave.capitalize()}: {valor}")

# Menu de opcines para operar

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opciomn: ").lower()

        if opcion == "1":
            registrar_ticket()
        elif opcion == "2":
            cambiar_estado()
        elif opcion == "3":
            generar_reporte()
        elif opcion == "4":
            listar_tickets()
        elif opcion == "5":
            print("Saliendo del sistema... Bye")
            break
        else:
            print("Seleccion invalida pon una opcion nuevamente")


if __name__ == "__main__":
    main()