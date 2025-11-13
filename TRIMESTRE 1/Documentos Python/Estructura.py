
Usuarios = {}

def menu(): 
    
    while True: 
        print ("0. Salir del Programa")
        print ("1. Resgistro")
        print ("2. Incio de Sesion")
        
        opcion = input("--Ingrese una Opcion--: ")
        if opcion == "0":
            print("Saliendo del Sistema")
            break
            
        elif opcion == "1":
            usuario = input("Ingrese su Usuario ")
            contraseña = int(input("Ingrese su Contraseña "))
            Usuarios[usuario] = contraseña
            print("Usuario Registrado Con exito.✅")
            
        elif opcion == "2":
            
            print("Inciando Sesion")
            
            usuario = input("Ingrese su usuario ")
            contraseña = int(input("Ingrese su Contraseña "))
            
            if usuario in Usuarios and Usuarios[usuario] == contraseña:
                print("Usuario Correcto.✅")
                
            else:
                print ("Intente de Nuevo")
                break 
            
            while True:
                print("0. Salir ")
                print("1. Juegos Matematicos")
                print ("2. Juegos Didacticos e interaccion")
                
                sub_opcion = input("Seleccione una Opcion: ")
                
                if sub_opcion == "0":
                    print("Saliendo")
                    break
                    
                elif sub_opcion == "1":
                    
                    while True: 
                        print("0. Salir..")
                        print("1. Sumar dos números.")#mate
                        print("2. Verificar si un numero es par o impar.")#mate
                        print("3. Diferencia de Numeros. ")#mate
                        print ("4. Determinar si un numero es positivo y negativo.")#mate
                        print ("5. Adivinar un Numero que Manda el Sistema.")#mate 
                        
                        
                        sub2_opcion = input("Seleccione Una Opcion: ")#Menu de interracion de matematicas 
                        
                        if sub2_opcion == "0":
                            break
                        
                        elif sub2_opcion == "1":
                            nmero = int(input("Ingrese su Primer Numero: "))
                            nmero2 = int(input("Ingrese el Segundo Numero: "))
                            suma = nmero + nmero2
                            print("La Suma entre los dos numeros es ",suma )

                        elif sub2_opcion == "2":
                            nmero0 = input("Ingrese su Primer Numero: ")

                            if nmero0 %2 == 0 :
                                print (f"Tu numero {nmero0} es par")
                            else:
                                print(f"Tu numero {nmero0} es impar")
                                
                        elif sub2_opcion == "3":
                            numero1 = int(input("Ingrese un numero: ")) 
                            numero2 = int(input(f"Ingrese otro numero mayo que el numero anterior:{numero1} "))
                            print ( "la diferencia entre ", numero2, " y ", numero1, " es: ", numero2 - numero1)
                            
                        elif sub2_opcion == "4":
                            numeroPositivo = int(input("Ingrese un numero positivo: "))
                        
                            if  numeroPositivo >= 0: 
                                print ("el numero es positivo")
                            else:
                                print ("el numero es negativo")
                            
                        elif sub2_opcion == "5":
                            from random import randint

                            intentos = 0
                            estimado = 0 
                            Nmero_secreto = randint (1, 100) 
                            Nombre = input("Dime Tu Nombre: ")
                            print(f"Bueno mi Querido {Nombre}, Estoy pensando en un numero")
                            while  intentos < 9:
                            
                                estimado = int(input("Cual es tu Numero?: "))
                        
                                intentos += 1
            
                            if estimado > 120 or estimado < 0:
                                print("Su numero esta fuera del rango, Porfavor ingrese otro Numero")
            
                            elif estimado < Nmero_secreto:
                                print ("Mi numero es mas alto") 
            
                            elif estimado > Nmero_secreto: 
                                print("Mi numero es mas Bajo")
            
                            else:
                                print (f"Felicidades {Nombre} Has adivinado el numero en {intentos} intentos ")
                                break 
            
                            if estimado != Nmero_secreto:
                                print (f"Lo siento has acabado el numero de intentos, el numero era {Nmero_secreto}")
                        
                                
                elif sub_opcion == "2":
                    while True:
                        print("0. Salir ")
                        print("1. Mezcla de Colores")
                        print("2. Sugerencia de Acciones")
                        
                        sub3_opcion = input("Ingrese una opcion: ")
                    
                        if sub3_opcion == "0":
                            print("Saliendo del Sitema")
                            break 
                        
                        elif sub3_opcion == "1":
                            print("Este programa mezcla dos colores.")
                            print(" r. Rojo      a. Azul")
                            primera = input("Elija un color (r o a): ")

                            if primera == "r":
                                print(" a. Azul      v. Verde")
                                segunda = input("Elija otro color (a o v): ")
                            if segunda == "a":
                                print("La mezcla de Rojo y Azul produce Magenta.")
                            elif segunda == "v":
                                print("La mezcla de Rojo y Verde produce Amarillo.")
                            elif primera == "a":
                                print(" v. Verde      r. Rojo")
                                segunda = input("Elija otro color (v o r): ")
                            if segunda == "v":
                                print("La mezcla de Azul y Verde produce Cian.")
                            elif segunda == "r":
                                print("La mezcla de Azul y Rojo produce Magenta.")
                            else:
                                print("Opción inválida para colores.")
                            
                        elif  sub3_opcion == "2":
                            hora = input("Escriba la Hora. Mañana, Tarde, Noche: ")
                            clima = input("Escriba el clima del dia, Soleado, Lluvioso, Nublado: ")
                            estado = input ("Escribe Tu estado de Animo Activo o Alegre: ")

                            if clima == "soleado" and hora == "mañana"  and estado == "activo":
                                print ("Deberias ir a hacer ejercicio")

                            elif clima == "lluvioso" and hora == "tarde" or  estado == "alegre" or estado == "Activo":
                                print(" Deberías leer")

                            elif clima == "nublado" and hora == "noche" and (estado == "activo" or estado == "alegre"):
                                print(" Deberías escuchar música animada")

                            elif clima == "soleado" and hora == "tarde" and estado == "alegre" or estado == "activo":
                                print(" Deberías salir con amigos")

                            elif clima == "nublado" and hora == "tarde" or estado == "activo" or estado =="alegre":
                                print(" Deberías ver una película o serie")
            
                            else:
                                print(" No hay actividad recomendada para esa combinación.")
                                
                elif sub2_opcion == "3":
                    while True:
                        print("0. Salir ")
                        print("1. ")
                        print("2. ")
                        
                        sub4_opcion = input("Ingrese una opcion: ")
                    
                        if sub4_opcion == "0":
                            print("Saliendo del Sitema...")
                            break 
                        
                        elif sub4_opcion == "1":
                            print("hola")
menu()