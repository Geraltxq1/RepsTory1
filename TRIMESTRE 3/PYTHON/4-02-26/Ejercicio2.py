total = 0
incidentes = 0
requerimiento = 0
premium = 0
escalados = 0
tiempo_total = 0
inmediatos = 0
prioritarios = 0
normales = 0
id = int(input("ID caso: "))

while id != 0:
    
    tipo = input("Tipo (incidente/requerimiento): ").lower().strip()  #lowe me pone todo en minusculas, strip quita estapacios
    while tipo not in  ("incidente", "requerimiento"):    # Hace la validacion de la opcion sino no deja seguir
        print("Eleccion mala ingrese Nuevamente")
        tipo = input("Tipo (incidente/requerimiento): ").lower().strip()  #lowe me pone todo en minusculas, strip quita estapacios

    prioridad = input("Prioridad (alta/media/baja): ").lower().strip()
    while prioridad not in  ("alta", "media", "baja"):    # Hace la validacion de la opcion sino no deja seguir
        print("Eleccion mala ingrese Nuevamente")
        prioridad = input("Prioridad (alta/media/baja): ").lower().strip()
        
    tiempo = int(input("Tiempo (min): "))
    
    es_premium = input("Premium (si/no): ")
    while es_premium not in  ("si", "no"):    # Hace la validacion de la opcion sino no deja seguir
        print("Eleccion mala ingrese Nuevamente")
        es_premium = input("Premium (si/no): ")

        
    puntaje = 0
    
    if prioridad == "alta":
        puntaje = 3
    elif prioridad == "media":
        puntaje = 2
            
    elif prioridad == "baja":
        puntaje = 1    
        
    if tipo == "incidente":
        puntaje += 1
        incidentes += 1
        
    if tipo == "requerimiento":
        puntaje += 1
        requerimiento += 1
        
    if es_premium == "si":
        puntaje += 2
        premium = premium + 1
    tiempo_total = tiempo_total + tiempo
    total += 1
        
    if tiempo > 120:
        print("Escalamiento")
        escalados += 1
    else:
        if puntaje >= 6:
            print("Inmediata")
            inmediatos = inmediatos + 1
        elif puntaje >= 4:
            print("Prioritaria")
            prioritarios += 1
        else:
            print("Normal")
            normales += 1

    id = int(input("ID caso: ")) 
    
if total >0:
    promedio = tiempo_total / total
else:
    print("No hay promedio")
print("Total casos:", total)
print("Incidentes:", incidentes)
print("Requerimientos:", requerimiento)
print("Premium:", premium)
print("Escalados:", escalados)
print("Promedio tiempo:", promedio)
print("Clasificación:", inmediatos, prioritarios, normales)
