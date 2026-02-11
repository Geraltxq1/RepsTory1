aprobados = 0
reprobados = 0
estudiantes = 0

print("Notas de Estudiantes Aprobados o Reprobados")
nombre = input("Ingrese el Nombre del Estudiante: ")
estudiantes +=1

nota = int(input("Ingrese la nota del alumno: "))

if nota >=3: 
    print("Alumno Aprobado")
    aprobados +=1
    
else:
    print("Alumno Reprobado")
    reprobados +=1
    
print("Reprobados:", reprobados)
print("Aprobados:", aprobados)
print("Estudiante Registrado", estudiantes)