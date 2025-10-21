
var  a;
var b;
a = parseInt(prompt("Ingrese un valor"))
b = parseInt(prompt("Ingrese un valor "))

var suma = a + b
var resta = a - b 
var multi  = a* b
var divi = a /b 
var modulo = a % b 

document.writeln("La suma de los numero es "+ suma + "<br>")
document.writeln("La resta de los numero es "+ resta + "<br>")
document.writeln("La multiplicacion de los numero es "+ multi + "<br>")
document.writeln("La division de los numero es "+ divi + "<br>")
document.writeln("El modulo de los numero es "+ modulo + "<br>")

var base;
var altura;
var area;

base = parseInt(prompt("Ingrese la base"))
altura = parseInt(prompt("Ingrese la altura"))

area = (base * altura )/ 2 

document.writeln("El area de el triangulo es "+ area+ "<br>")

var cat1;
var cat2;

cat1 = parseInt(prompt("ingrese el cateto1 "))
cat2 = parseInt(prompt("Ingrese el Cateto2 "))

hipot = Math.sqrt(cat1**2 + cat2**2)

document.writeln("La hipotenusa es "+ hipot + "<br>")

var grados;

grados = parseInt(prompt("Ingrese los Grados"))

faren = (grados*9/5)+32

document.writeln("Los grados celcius a fahrenheit es "+ faren)