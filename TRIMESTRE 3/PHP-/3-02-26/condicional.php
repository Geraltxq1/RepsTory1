<?php
//estructuras de control condicionales 

$nombre = "juan";
$edad = 17;
$mayoria_edad = 18;

if($edad >= $mayoria_edad){
    echo "<h1>$nombre es mayor de edad </h1>";

}else{
    echo "<h1>$nombre es menor de edad"
}


$edad = 18;
$edad1 = 25;
$edad2 = 15;

if ($edad2 >= $edad && $edad2 <= $edad1){
    echo "<h2> Esta en edad de trabajar </h2>";
}else{
    echo "<h2> No esta en edad de trabajar</h2>";
}

echo"<hr>";
//operador || (OR)
$pais = "colombia";
if ($pais == "mexico" || $pais == "colombia" || $pais == "españa"){
    echo "<h2>"
}