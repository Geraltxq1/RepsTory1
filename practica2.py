reprobados = 0
aprobados = 0
nota_mas_alta = 0
suma_notas = 0
contador = 0

estudiante = input("Ingrese el nombre del Estudiante: ")

while estudiante != "FIN":
    nota = float(input("Ingrese la nota del Estudiante: "))
    
    suma_notas += nota
    contador += 1

    if nota > 3:
        aprobados += 1
    else:
        reprobados += 1

    if nota > nota_mas_alta:
        nota_mas_alta = nota

    print("-------------------|-----------------|-------------------")
    estudiante = input("Ingrese el nombre del Estudiante: ")

if contador > 0:
    promedio = suma_notas / contador
else:
    promedio = 0

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Nota más alta:", nota_mas_alta)
print("Promedio general:", promedio)