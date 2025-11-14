var health = 100
var maxHealth = 100
var bar = document.getElementById("health")
var messageBox = document.getElementById("message")
var flash = document.getElementById("flash")


function limit(v) {
    return Math.min(Math.max(v, 0), maxHealth)
}

function attack(amount, audioId, element, heal, powerName) {
    var h = Math.abs(heal * 1)        
    var ajuste = amount * (h * 2 - 1) 

    health = limit(health + ajuste)
    bar.style.width = health + "%"

    var r = 255 - Math.floor((health / 100) * 200)
    var g = Math.floor((health / 100) * 200)
    bar.style.background = "rgb(" + r + "," + g + ",60)"

    document.getElementById(audioId).play()

    element.classList.add("active")
    setTimeout(function () {
        element.classList.remove("active")
    }, 300)

    flash.style.animation = "none"
    void flash.offsetHeight
    flash.style.animation = "flashAnim 0.5s forwards"

    var textoA = "💚 Has usado " + powerName + " y recuperaste " + amount + " de poder."
    var textoB = "⚔️ Has sido atacado con: " + powerName + " y te bajó " + amount + " de poder."
    

    var mensaje = (textoA + "").repeat(h) + (textoB + "").repeat(1 - h)

    messageBox.innerHTML = mensaje

    messageBox.classList.remove("show")
    void messageBox.offsetWidth
    messageBox.classList.add("show")
}

