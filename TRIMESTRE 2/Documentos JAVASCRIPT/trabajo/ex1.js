///
console.log("Esto es ex1.js");

///
var nombre = "Carlos";
var apellido = "Ortiz";
var fecha_nacimiento = 2007;
var edad = 2025 - fecha_nacimiento;
var mensaje = " Hola, mi nombre es " + nombre +" "+ apellido +  ", tengo "  + edad +  " años, y estoy aprendiendo Javascript."

document.getElementById("student_message").innerHTML = mensaje;

///
var num1 = parseFloat(document.getElementById("num_1").textContent);
var num2 = parseFloat(document.getElementById("num_2").textContent);
var promedio = ((num1 + num2) / 2) .toFixed(2);
document.getElementById("result").textContent = promedio;


///
var phone1 = "988866552";
var phone2 = "99087612366";
var phone3 = "876543123";

console.log ("El numero " + phone1 + " es " + (phone1.length ===9 ));
console.log ("El numero " + phone2 + " es " + (phone2.length ===9 ));
console.log ("El numero " + phone3 + " es " + (phone3.length ===9 ));


///
var num1 = 32
var num2 = 6
var operacion = num1 ** num2
console.log(operacion)

///

    var quantity = "25";
    var number = 6;
    var pressure;
    var temperature = null;

    console.log(quantity += quantity); 
    console.log( (7+5) / number + 2 ); 
    console.log(pressure); 
    console.log(temperature); 
    console.log(typeof pressure); 
    console.log(typeof temperature);

