<?php

/**
 * Script de configuración inicial.
 * Crea la base de datos y la tabla necesarias.
 */

require_once __DIR__ . '/config.php';

try {
    // 1. Conectamos a MySQL sin especificar base de datos
    $dsn = "mysql:host=" . DB_HOST . ";charset=" . DB_CHARSET;
    $options = [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ];

    $pdo = new PDO($dsn, DB_USER, DB_PASS, $options);

    // 2. Creamos la base de datos si no existe
    $pdo->exec("CREATE DATABASE IF NOT EXISTS " . DB_NAME);
    echo "<p>Base de datos '<b>" . DB_NAME . "</b>' verificada/creada exitosamente.</p>";

    // 3. Seleccionamos la base de datos
    $pdo->exec("USE " . DB_NAME);

    // 4. SQL para crear la tabla
    $sql = "
        CREATE TABLE IF NOT EXISTS ventas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            producto VARCHAR(200) NOT NULL,
            monto DECIMAL(10, 2) NOT NULL,
            fecha DATE NOT NULL,
            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ";

    $pdo->exec($sql);

    echo "<p>Tabla '<b>ventas</b>' verificada/creada exitosamente.</p>";
    echo "<p><a href='index.php'>Ir al inicio</a></p>";

} catch (PDOException $e) {
    http_response_code(500);
    echo "<h2>Error en la configuración</h2>";
    echo "<p>Error: " . htmlspecialchars($e->getMessage()) . "</p>";
    echo "<p>Verifica:</p>";
    echo "<ul>
        <li>Que MySQL esté corriendo (XAMPP).</li>
        <li>Que el usuario y contraseña en config.php sean correctos.</li>
    </ul>";
}
?>