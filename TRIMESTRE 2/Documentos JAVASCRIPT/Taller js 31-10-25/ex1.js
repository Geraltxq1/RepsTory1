/// Ejercicio 1 - Resultado por consola
console.log("Esto es ex1.js");

/// Ejercicio 2 
var nombre = "Carlos";
var apellido = "Ortiz";
var fecha_nacimiento = 2007;
var edad = 2025 - fecha_nacimiento;
var mensaje = " Hola, mi nombre es " + nombre +" "+ apellido +  ", tengo "  + edad +  " años, y estoy aprendiendo Javascript."

var mensajeDiv = document.getElementById("student_message");

mensajeDiv.addEventListener("click", function () {
    mensajeDiv.innerHTML = mensaje
});

/// Ejercicio 3 

var num1 = parseFloat(document.getElementById("num_1").innerHTML);
var num2 = parseFloat(document.getElementById("num_2").innerHTML);
var promedio = ((num1 + num2) / 2) .toFixed(2);

var primedioDiv = document.getElementById("result");

primedioDiv.addEventListener("click", function (){
    primedioDiv.innerHTML = promedio
}
)

/// Ejercicio 4 - Resultados por consola
var phone1 = "988866552";
var phone2 = "99087612366";
var phone3 = "876543123";

console.log ("El numero " + phone1 + " es " + (phone1.length ===9 ));
console.log ("El numero " + phone2 + " es " + (phone2.length ===9 ));
console.log ("El numero " + phone3 + " es " + (phone3.length ===9 ));


/// Ejercicio 5 - Resultado en consola
var num1 = 32
var num2 = 6
var operacion = num1 ** num2
console.log(operacion)

/// Ejercicio 7 - Resultados por consola

    var quantity = "25"; 
    var number = 6;   
    var pressure;
    var temperature = null;

    console.log(quantity += quantity); /// 2525
    console.log( (7+5) / number + 2 ); /// 4
    console.log(pressure);             /// undefined       /// resultados que dio la consola
    console.log(temperature);          /// null            /// 
    console.log(typeof pressure);      /// Undefined 
    console.log(typeof temperature);   /// Object 


/// Ejercicio 8

var url1Div = document.getElementById("url_1");
var url2Div = document.getElementById("url_2");
var url3Div = document.getElementById("url_3");
var url4Div = document.getElementById("url_4");

url1Div.addEventListener("click", function() {
    var url1 = url1Div.innerHTML.trim();
    url2Div.innerHTML = "https://" + url1;
});

url3Div.addEventListener("click", function() {
    var url3 = url3Div.innerHTML.trim();
    url4Div.innerHTML = url3.replace("https://", "");
});

/// 
