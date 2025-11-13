"""
Ingrese una nota, si la nota esta en 
0 <= 3 reprobado
3 <= 4 Aprobado
4 <= 5 Excelente
""" 


Ldos = float(input("Ingrese un numero de lados entre 3 y 6: "))
match Ldos:
    case 3:
        if Ldos == 3:
            print("El Lado correspondiente es al triangulo")
    case 4:
        if Ldos == 4:
            print("El Lado correspondiente es al Cuadrado")
            
    case 5:        
        if Ldos == 5 :
            print("El Lado correspondiente es al Pentagono ")
            
    case 6:        
        if Ldos == 6 :
            print("El Lado correspondiente es al hexagono ")
    
    case _: 
        print("Opcion Invalida")



comandos = input("Ingrese el comando a correr: ")
match comandos :
        
case "Star":
        print("Programa Iniciado")
case "Stop":
        print("Programa Detenido")
case "Pause":
        print("Programa Pausado")
case "Exit":
        print("Programa Cerrado")
        
        
        
semaforos = input("Ingrese el estado del Semaforo: ")
a = "rojo"
b = "amarillo"
c = "verde"
match semaforos:

case "a":
        print("Estado del Semaforo: ", a)
case "b":
        print("Estado del Semaforo: ", b)
case "c":
        print("Estado del Semaforo: ", c)





