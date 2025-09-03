from unittest import case

print ("Hola, bienvenido al sistema")

Usuario = input ("Ingrese su Usuario ")

if Usuario == "Char0301":
    print("Usuario Correcto")
else:
    print ("Usuario Incorrecto")
    print ("Intente de Nuevo")


contraseña = input("Ingrese su contraseña: ")

if contraseña == "carlos2003.":
    print("Bienvenido")
    print ("Que Bueno verte de Nuevo CARLOS")
    print ("Que quieres hacer Hoy, Acontimuacion Te dare un Menu de Interaccion..")
    
else:
    print("Contraseña incorrecta")
    print ("Usuario Incorrecto")
    print ("-----------------------------------------------------")
    exit()

print ("---------------------------------------------------------") 


def menu ():
    while True :
        print ("0. Salir ")
        print ("1. Juegos Matematicos ")
        print ("2. Juegos Didacticos ")
        
        opcion = input("Seleccione una Opcion ")
        
        
        if opcion == "1":
            
            while True:
                print("0. Salir" )
                print("1. Sumar dos números")#mate
                print("2. Verificar si un numero es par o impar")#mate
                print("3. Diferencia de Numeros ")#mate
                print("4. Determinar si un Numero es Positivo o Negativo ")#mate
                print("5. Adivinar un Numero")#mate
                print("6. VACIO")
                
                sub_opcion = input("Seleccione una opcion: ")

                match sub_opcion:
                    case "0":
                        print("Saliendo del Sistema..")
                        break

                    case "1":
                        num1 = int(input("Ingrese el primer numero: "))
                        num2 = int(input("Ingrese el segundo numero: "))
                        suma = num1 + num2
                        print(f"La suma de {num1} y {num2} es: {suma}")
                        
                    case "2":
                        num = int(input("Ingrese un numero: "))
                        if num % 2 == 0:
                            print(f"El numero {num} es par.")
                        else:
                            print(f"El numero {num} es impar.")
                    
                            
                    case "4":
                        numero1 = int(input("Ingrese un numero: ")) 
                        numero2 = int(input(f"Ingrese otro numero mayo que el numero anterior:{numero1} "))
                        print ( "la diferencia entre ", numero2, " y ", numero1, " es: ", numero2 - numero1)
                    
                    case "5":
                        
                        numeroPositivo = int(input("Ingrese un numero positivo: "))
                        if  numeroPositivo >= 0: 
                            print ("el numero es positivo")  

                        else : 
                            print ("el numero es negativo")    
                            print ("gracias por participar en el sistema del SENA")
                            print ("fin del programa")
                            print ("vuelve pronto")
                            print ("fin del programa.....")
                            
                    case "6":
                        from random import randint

                        intentos = 0
                        estimado = 0 
                        Nmero_secreto = randint (1, 100) 
                        Nombre = input("Dime Tu Nombre ")
                        print(f"Bueno mi Querido {Nombre}, Estoy pensando en un numero")
                        while  intentos < 9:
                            
                            estimado = int(input("Cual es tu Numero? "))
                        
                            intentos += 1
            
                            if estimado > 120 or estimado < 0:
                                print("sU NUMERO ESTA FUERA DEL RANGO, INGRESE OTRO NUMERO")
            
                            elif estimado < Nmero_secreto:
                                print ("Mi numero es mas alto") 
            
                            elif estimado > Nmero_secreto: 
                                print("Mi numero es mas Bajo")
            
                            else:
                                print (f"Felicidades {Nombre} Has adivinado el numero en {intentos} intentos ")
                                break 
            
                        if estimado != Nmero_secreto:
                            print (f"Lo siento has acabado el numero de intentos, el numero era {Nmero_secreto}")
                        
                            
                    case "8":
                        print("VACIO")        
                            
                    

                    case _:
                    
                        print("Opción no válida. Por favor, intente de nuevo.") 
                        
        if opcion == "2":
            
            while True:
                print ("0. Salir")
                print ("1. Mezcla de Colores")
                print ("2. Sugerencias de Acciones")
                
                sub2opcion = input("Seleccione Una Opcion")
                
                match sub2opcion:
                    
                    case "0":
                        
                        print("Saliendo")
                        break
                    
                    case "1":
                        
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
                        
                    case"2":
                        
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
                    
                    
                    
                    case _:
                        print ("Opcion no Valida. Por favor, Intente de Nuevo")
                   
                        
menu()  