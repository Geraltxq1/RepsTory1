
function sumar() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = n1 + n2;
    document.getElementById("resultado").innerHTML =
        "La suma del número " + n1 + " y el número " + n2 + " es: " + resultado;
}

function restar() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = n1 - n2;
    document.getElementById("resultado").innerHTML =
        "La resta de " + n1 + " menos " + n2 + " es: " + resultado;
}

function multiplicar() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = n1 * n2;
    document.getElementById("resultado").innerHTML =
        "La Multiplicacion de " + n1 + " por " + n2 + " es: " + resultado;
}

function dividir() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = n1 / n2;
    document.getElementById("resultado").innerHTML = "La división de " + n1 + " entre " + n2 + " es: " + resultado;
}

function area() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = (n1 * n2)/2;
    document.getElementById("resultado").innerHTML = " La Base " + n1 + " y Altura " + n2 + " da un Area de: " + resultado;

}


function hipo() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = Math.sqrt(n1**2 + n2**2);
    
    document.getElementById("resultado").innerHTML = "El cateto 1 = " + n1 + " y cateto 2 = " + n2 + ", la hipotenusa es: " + resultado.toFixed(2);
}


function grados(){
    var n1 = parseFloat(document.getElementById("num1").value);
    var resultado = (n1 * 9/5) + 32
    document.getElementById("resultado").innerHTML = "La conversion de los Grados: " + n1 + " es igual a : " + resultado.toFixed(2);
}

