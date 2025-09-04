
Usuarios = {}

def menu():
    
    while True: 
        print ("0. Salir del Programa")
        print ("1. Resgistro")
        print ("2. Incio de Sesion")
        
        opcion = input("--Ingrese una Opcion--")
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
                
                sub_opcion = input("Seleccione una Opcion")
                
                if sub_opcion == "0":
                    print("HOLA")
                    
                elif sub_opcion == "1":
                    
                    while True: 
                        print("0. Salir")
                        print("1. Sumar dos números")#mate
                        print("2. Verificar si un numero es par o impar")#mate
                        print("3. Diferencia de Numeros ")#mate 
                        
                        sub2_opcion = input("Seleccione Una Opcion")
                        
                        if sub2_opcion == "o":
                            break
                        
                        elif sub2_opcion == "1":
                            nmero = int(input("Ingrese su Primer Numero "))
                            nmero2 = int(input("Ingrese el Segundo Numero "))
                            suma = nmero + nmero2
                            print("La Suma entre los dos numeros es ",suma )

                        elif sub2_opcion == "2":
                            nmero0 = input("Ingrese su Primer Numero ")

                            if nmero0 %2 == 0 :
                                print (f"Tu numero {nmero0} es par")
                            else:
                                print(f"Tu numero {nmero0} es impar")
                                
                        elif sub2_opcion == "3":
                            print("")
                            
                            
                            
                elif sub_opcion == "2":
                    while True:
                        print("0. Salir ")
                        print("1. Mezcla de Colores")
                        print("2. Sugerencia de Acciones")
                        
                        
                        
                        sub3_opcion = input("Ingrese una opcion")
                    
                        if sub3_opcion == "0":
                            print("Saliendo del Sitema")
                            break 
                        
                        if sub3_opcion == "1":
                            print("Inciando Ejercicio")
                            
                        if sub3_opcion == "2":
                            print("3")
                            

menu()


