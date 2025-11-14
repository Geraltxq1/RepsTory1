var personaje = document.getElementById("personaje");
var stats = document.getElementById("stats");

function barra(valor, color) {
    return "<div class='barra'><div class='relleno' style='width:" + valor + "%; background:" + color + ";'></div></div>";
}

function equipar(n) {

    switch(n) {

        case 1: 
            personaje.src = "image/cuero.png";
            stats.innerHTML =
                "Vida" + barra(60, "#b30000") +
                "Defensa" + barra(40, "#9e7700") +
                "Velocidad" + barra(80, "#0066ff");
            break;

        case 2: 
            personaje.src = "image/Hierro.png";
            stats.innerHTML =
                "Vida" + barra(80, "#b30000") +
                "Defensa" + barra(80, "#9e7700") +
                "Velocidad" + barra(40, "#0066ff");
            break;

        case 3: 
            personaje.src = "image/Oro.png";
            stats.innerHTML =
                "Vida" + barra(70, "#b30000") +
                "Defensa" + barra(60, "#9e7700") +
                "Velocidad" + barra(70, "#0066ff");
            break;

        case 4: 
            personaje.src = "image/Legendaria.png";
            stats.innerHTML =
                "Vida" + barra(100, "#b30000") +
                "Defensa" + barra(95, "#9e7700") +
                "Velocidad" + barra(90, "#0066ff");
            break;

        case 5: 
            personaje.src = "image/base.png";
            stats.innerHTML =
                "Vida" + barra(50, "#b30000") +
                "Defensa" + barra(20, "#9e7700") +
                "Velocidad" + barra(65, "#0066ff");
            break;
    }
}
