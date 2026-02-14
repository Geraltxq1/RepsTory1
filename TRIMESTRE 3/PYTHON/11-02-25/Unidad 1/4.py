print("Ejercicion nmro2")
aprobados = 0
reprobados = 0

print("Notas de Estudiantes Aprobados o Reprobados")
nombre = input("Ingrese el Nombre del Estudiante: ")

nmero_notas = int(input("Cuantas notas vas a Ingresar?: "))


notas = []

for nota in range(nmero_notas):
    
    nota = float(input("Ingrese las notas: "))
    notas.append(nota)

def calcular_promedio(notas):
    return sum(notas) / len(notas)

promedio = calcular_promedio(notas)

print("el promedio de ",nombre," es",promedio)

