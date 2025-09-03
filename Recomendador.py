hora = input("Escriba la Hora. Mañana, Tarde, Noche ")
clima = input("Escriba el clima del dia, Soleado, Lluvioso, Nublado ")
estado = input ("Escribe Tu estado de Animo Activo o Alegre ")

if clima == "soleado" and hora == "mañana"  and estado == "activo":
    print ("Deberias ir a hacer ejercicio")

elif clima == "lluvioso" and hora == "tarde" or  estado == "alegre" or estado == "Activo":
    print(" Deberías leer")

elif clima == "nublado" and hora == "noche" and (estado == "activo" or estado == "alegre"):
    print(" Deberías escuchar música animada")

elif clima == "soleado" and hora == "tarde" and estado == "alegre":
    print(" Deberías salir con amigos")

elif clima == "nublado" and hora == "tarde" and estado == "activo":
    print(" Deberías ver una película o serie")
    
else:
    print(" No hay actividad recomendada para esa combinación.")
