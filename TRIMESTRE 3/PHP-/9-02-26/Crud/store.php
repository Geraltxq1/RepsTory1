<?php

/**
 * procesa el formulario de creacion de una nueva venta.
 * usar el isset() para verificar que los campos existan.
 * validar las reglas de negocio, como que el monto sea numero positivo y 
 * el producto no este vacio.
 * archivo de conexion a la base de datos
 * recordar configurar su bd en Mysql
 */


require_once __DIR__ . '/db.php';
require_once __DIR__ . '/helpers.php';


// verificamos el envio POST

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    
    redirect('index.php');
    
}

// validacion con isset()

$requieredFields = ['producto', 'monto', 'fecha'];

foreach ($requieredFields as $f) {
    if (!isset($_POST[$f])) {
        // si falta algun campo requerido, redirigimos a index.php
        $errors = ['general' => "Faltan campos requeridos. $f"];
        $qErrors = base64_encode(json_encode($errors));
        redirect("index.php?errors=$qErrors");
    }
}

// normalizar los datos del formulario ()limpiar

$data = [
    'producto' => trim($_POST['producto']),
    'monto' => trim($_POST['monto']),
    'fecha' => trim((string) $_POST['fecha']),
];

// validamos las reglas de negocio (longitud, numerico, formato de fecha etc.)

$errors = validateVenta($data);

if (!empty($errors)) {

    // si hay errores, redirigimos a index.php con los errores en la query string
    $qErrors = base64_encode(json_encode($errors));
    $qOld = base64_encode(json_encode($data));
    redirect("create.php?errors=$qErrors&old=$qOld");
}

// insertamos el la BD

try {
    $pdo = getPDO();
    $sql = "INSERT INTO ventas (producto, monto, fecha) VALUES 
    (:producto, :monto, :fecha)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        'producto' => $data['producto'],
        'monto' => $data['monto'],
        'fecha' => $data['fecha'],
    ]);

    redirect("index.php");

} catch (PDOException $e) {
    
    http_response_code(500);
    echo "<h3>Error al guardar la venta</h3> ";
    echo "<p>" . $e->getMessage() . "</p>";
    echo "<p><a href='create.php'>Volver</a></p>";
   
}

?>