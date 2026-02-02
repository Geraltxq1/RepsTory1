var elementos = [];

function mostrarTareas() {
    var lista = document.getElementById("lista");
    lista.innerHTML = "";

    elementos.forEach(function(item){
    lista.innerHTML += "<li>" + item + "</li>";
    });
}

function AgregarInico() {
    var campo = document.getElementById("entrada");
    var valor = campo.value.trim();

    if (valor === "") return;

    elementos.unshift(valor);
    campo.value = "";

    mostrarTareas();
}

function AgregarFinal() {
    var campo = document.getElementById("entrada");
    var valor = campo.value.trim();

    if (valor === "") return;

    elementos.push(valor);
    campo.value = "";

    mostrarTareas();
}

function QuitarInicio() {
    elementos.shift();
    mostrarTareas();
}

function QuitarFinal() {
    elementos.pop();
    mostrarTareas();
}