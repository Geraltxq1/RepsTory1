<?php

/**
 * configurar la funcion PDO nos permite conectarnos a la base de datos
 * y ejecutar consultas SQL manejo de errores y expcepciones.
 * Al ocurrir un error nos lanza excepciones que podemos manejar con try catch.
 * PDO nos ayuda a manejar errores de manera robusta y segura.
 */

require_once __DIR__ . '/config.php';

/**
 * Funcion para obtener una conexion PDO a la base de datos
 * retorna una instancia de la BD
 * @return PDO
 */


function getPDO(): PDO
{
    static $pdo = null;

    // si ya existe una conexion, la retornamos

    if ($pdo instanceof PDO) {
        return $pdo;
    }

    // DSN (data source name) para la conexion PDO.
    $dsn = sprintf('mysql:host=%s;dbname=%s;charset=%s', 
        DB_HOST, 
        DB_NAME, 
        DB_CHARSET
    );

    // opciones para trabajar con PDO.

    $options = [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        // Manejo de errores con excepciones
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        // Modo de obtencion de datos como array asociativo
        PDO::ATTR_EMULATE_PREPARES => false,
        // Desactiva la emulacion de sentencias preparadas
    ];

    // se crea la conexion
    try {
        $pdo = new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        throw new PDOException($e->getMessage(), (int)$e->getCode());
    }

    return $pdo;
}

