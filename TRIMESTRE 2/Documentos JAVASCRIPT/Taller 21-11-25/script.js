var nombres = [
    "Carlos",
    "Yeral",
    "Juan",
    ["Sebastian ", " Alex"],
    "Juan David ",
    "Laura",
    "Silvana ",
    "Andres"
];

var contenedor = document.getElementById("resultado");

nombres.forEach(function(nombre, indice) {
    console.log(+ indice + " - posicion: " + nombre);
    
    contenedor.innerHTML = 
        contenedor.innerHTML + 
        indice + " - posicion: " + nombre + "<br>";
});


