print ("Hola bienvenido al sistema ")

edad =  int(input("Ingrese su edad "))
genero = input("Ingrese su genero ")


if edad >= 18 and edad <= 25 and genero == "M":

    print ("Usted es apto para el servicio militar ")
    
else:
    print ("Usted no es apto")