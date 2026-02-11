<?php
echo "<h1>Ejercicios</h1>";

// 1. País y continente
echo "<h2>1. País y Continente</h2>";
$pais = "Colombia";
$continente = "América";
echo "Vivo en " . $pais . " y está en " . $continente;

// 2. Números pares del 1 al 100
echo "<h2>2. Números pares del 1 al 100</h2>";
for ($i = 1; $i <= 100; $i++) {
    if ($i % 2 == 0) {
        echo $i . " ";
    }
}

// 3. Cuadrados de los primeros 40 números
echo "<h2>3. Cuadrados de los primeros 40 números</h2>";
for ($i = 1; $i <= 40; $i++) {
    echo "El cuadrado de $i es " . ($i * $i) . "<br>";
}

// 4. Calculadora con GET
echo "<h2>4. Calculadora con parámetros GET</h2>";
if (isset($_GET['num1']) && isset($_GET['num2'])) {
    $num1 = $_GET['num1'];
    $num2 = $_GET['num2'];

    echo "Número 1: $num1<br>";
    echo "Número 2: $num2<br>";
    echo "Suma: " . ($num1 + $num2) . "<br>";
    echo "Resta: " . ($num1 - $num2) . "<br>";
    echo "Multiplicación: " . ($num1 * $num2) . "<br>";

    if ($num2 != 0) {
        echo "División: " . ($num1 / $num2) . "<br>";
    } else {
        echo "No se puede dividir por cero<br>";
    }
} else {
    echo "Usa la URL así: ?num1=10&num2=5<br>";
}

// 5. Números entre dos valores GET
echo "<h2>5. Números entre dos valores (GET)</h2>";
if (isset($_GET['inicio']) && isset($_GET['fin'])) {
    $inicio = $_GET['inicio'];
    $fin = $_GET['fin'];

    for ($i = $inicio; $i <= $fin; $i++) {
        echo $i . " ";
    }
} else {
    echo "Usa la URL así: ?inicio=5&fin=15<br>";
}

// 6. Tabla de multiplicar 1 al 10
echo "<h2>6. Tablas de multiplicar del 1 al 10</h2>";
echo "<table border='1' cellpadding='10'>";
echo "<tr>";

for ($i = 1; $i <= 10; $i++) {
    echo "<th>Tabla del $i</th>";
}

echo "</tr><tr>";

for ($i = 1; $i <= 10; $i++) {
    echo "<td>";
    for ($j = 1; $j <= 10; $j++) {
        echo "$i x $j = " . ($i * $j) . "<br>";
    }
    echo "</td>";
}

echo "</tr></table>";
?>


