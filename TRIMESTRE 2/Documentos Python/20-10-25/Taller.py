# Carlos Andres Ortiz, Juan Sebastian Rivera
print("Analizador")

Texto = input("Ingrese un Texto: ").lower()
Ltras1 = input("Ingrese Una Letra: ").lower()
Ltras2 = input("Ingrese Una Letra: ").lower()
Ltras3 = input("Ingrese Una Letra: ").lower()

Ltras1_lower = Ltras1.lower()
Ltras2_lower = Ltras2.lower()
Ltras3_lower = Ltras3.lower()

print(Texto.count(Ltras1.lower()))
print(Texto.count(Ltras2.lower()))
print(Texto.count(Ltras3.lower()))

print("="*70)

Lista_Nuestra = [Ltras1, Ltras2, Ltras3]
print(Lista_Nuestra)

print("="*70)

palabras = Texto.split()
cantidad_palabras = len(palabras)
print(cantidad_palabras)

print("="*70)

primeraLetra = Texto[0]
UltimaLetra = Texto[-1]

print(primeraLetra)
print(UltimaLetra)

print("="*70)

texto_inverso = Texto[::-1]
print("Texto invertido:", texto_inverso)