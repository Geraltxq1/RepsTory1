<?php


// Constantes no pueden cambiar su valor 

define("PI", 3.1416);
define("pulgada", 0.3937);
define("libra", 2.55);

$cm=50;
$kilo = 1000;

echo $cm* pulgada . "pulgadas\n";
echo $kilo * libra . "libras\n";

// Constantes

echo "Directorio actual:" . __DIR__ . "\n";
echo "Archivo actual:" . __FILE__ . "\n";
echo PHP_OS . "<BR>";
echo PHP_VERSION . "<br>";
echo PHP_EXTENSION_DIR . "<br>";
echo __LINE__ . "<br>";
echo __FILE__ . "<br>";

?>
