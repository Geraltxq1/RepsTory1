<?php 
/*
for (variable_inicio_:;)
*/

// sumar todos los numeros del 1 al 100

$resultado = 0;
// mientras q i sea menor o igual a 100

for($i = 1; $i <100; $i++){
    $resultado += $i; // resultado = resultado + i
    echo "<p> $resultado </p>";
}

echo "<h1 el resultado de la suma es: $resultado </h1>";

echo "<hr>";

// loop y envio con isset 
if(isset($_GET["numero"])){
    $numero = (int) $_GET ["numero"];

}else{
    $numero =2;
}
echo "<h1> Tabla de multiplicar del numero: $numero </h1>";

for ($contador = 1; $contador <= 10; $contador++){
    echo"$numero x $contador = ".($numero * $contador)."<br>";
}



?>