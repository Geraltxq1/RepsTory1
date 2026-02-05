<?php
/*
while (condicional)
bloque de instrucciones a ejecutar 
    estructura de control que itera o repite la ejecucion
    de una serie de instrucciones mientras se cumpla una condicion 
    1. Incializacion de la variable contador 
    2. condicion de entrada al bucle 
    3. Incremento o decremento de la variable contador 
*/
// se inicializa la variable en 0

$numero = 0; 

// bucle while mientras $numero sea menor o igual a 100
while($numero <= 100){
    echo "<P> $numero </p>";
    // incremento de la variable contador 
    $numero ++;

}

// reiniciamos la variable numero a = 0

$numero = 0; 
$resultado = 0;
while($numero <= 100)
    $resultado += $numero;
echo"<p> $resultado</p>";
$numero ++;

echo"<hr>";
echo"<h1> el resultado de la suma es: $resultado</h1>";

echo"<hr>";
$edad = 18;
$contador = 1; 

do{
    echo"<p> Tienes Acceseso a contenido Privado </p>";
    $contador++;


}while($edad<= 18 && $contador <= 5)

?>