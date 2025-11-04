
function sumar() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = n1 + n2;
    document.getElementById("resultado").innerText =
        "La suma del número " + n1 + " y el número " + n2 + " es: " + resultado;
}

function restar() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = n1 - n2;
    document.getElementById("resultado").innerText =
        "La resta de " + n1 + " menos " + n2 + " es: " + resultado;
}

function multiplicar() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    var resultado = n1 * n2;
    document.getElementById("resultado").innerText =
        "La Multiplicacion de " + n1 + " por " + n2 + " es: " + resultado;
}

function dividir() {
    var n1 = parseFloat(document.getElementById("num1").value);
    var n2 = parseFloat(document.getElementById("num2").value);
    if (n2 === 0) {
        document.getElementById("resultado").innerText = "No se puede dividir entre 0.";
    } else {
        var resultado = n1 / n2;
        document.getElementById("resultado").innerText =
            "La división de " + n1 + " entre " + n2 + " es: " + resultado;
    }
}
