
function mostrar(texto) {
    document.getElementById("resultado").innerHTML = texto;
}

function ejercicio1() {
    let num = parseInt(prompt("Ingrese un numero entero positivo:"));

    if(num >= 1 && num <= 9){
        mostrar("El numero tiene 1 digito");
    } else if(num >= 10 && num <= 99){
        mostrar("El numero tiene 2 dígitos");
    } else if(num >= 100 && num <= 999){
        mostrar("El numero tiene 3 digitos");
    } else if(num >= 1000 && num <= 9999){
        mostrar("El numero tiene 4 dígitos");
    } else {
        mostrar("Numero fuera de rango");
    }
}

function ejercicio2() {
    let a = parseFloat(prompt("Ingrese el primer numero:"));
    let b = parseFloat(prompt("Ingrese el segundo numero:"));
    let c = parseFloat(prompt("Ingrese el tercer numero:"));

    let menor = Math.min(a,b,c);
    mostrar("El numero menor es: " + menor);
}

function ejercicio3() {
    let n1 = parseFloat(prompt("Ingrese el primer numero:"));
    let n2 = parseFloat(prompt("Ingrese el segundo numero:"));
    let n3 = parseFloat(prompt("Ingrese el tercer numero:"));

    if(n1 < n2 && n2 < n3){
        mostrar("Los numeros estan en orden ascendente");
    } else if(n1 > n2 && n2 > n3){
        mostrar("Los numeros están en orden descendente");
    } else {
        mostrar("Los numeros no estan ordenados");
    }
}

function ejercicio4() {
    let sexo = prompt("Ingrese, si es Hombre H, si es Mujer M:").toUpperCase();
    let edad = parseInt(prompt("Ingrese edad:"));
    let tiempo = parseFloat(prompt("Ingrese el tiempo anterior minutos:"));

    if(sexo === "H"){
        if(edad < 40 && tiempo <= 150){
            mostrar("Atleta seleccionado.");
        } else if(edad >= 40 && tiempo <= 175){
            mostrar("Atleta seleccionado.");
        } else {
            mostrar("No cumple los requisitos.");
        }
    } else if(sexo === "M"){
        if(tiempo <= 180){
            mostrar("Atleta seleccionada.");
        } else {
            mostrar("No cumple los requisitos.");
        }
    } else {
        mostrar("Sexo no válido.");
    }
}

function ejercicio5() {
    let nombre = prompt("Ingrese el nombre del vendedor: ");
    let codigo = parseInt(prompt("Ingrese el codigo 1,2,3: "));
    let ventas = parseFloat(prompt("Ingrese el total de ventas: "));

    let comision = 0;

    switch(codigo){
        case 1: comision = ventas * 0.05; break;
        case 2: comision = ventas * 0.08; break;
        case 3: comision = ventas * 0.03; break;
        default:
            mostrar("Codigo invalido");
            return;
    }

    mostrar(`Vendedor: ${nombre}<br>Comision: $${comision.toFixed(2)}`); /* para qeu nos de dos decimales   */
}

