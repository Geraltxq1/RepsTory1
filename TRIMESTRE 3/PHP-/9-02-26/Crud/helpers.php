<?php

/**
 * Archivo de funciones auxiliares para el proyecto de ventas
 * contiene funciones para redireccionar, validar datos, etc.
 * estas funciones pueden ser usadas en todo el proyecto para evitar repetir codigo.
 * 
 * nos previene inyecciones de codigo al limpiar los datos de entrada.
 * @param string $data el dato a limpiar
 * @return string el dato limpio
 */


function h(?string $value): string
{
    return htmlspecialchars($value ?? '', ENT_QUOTES, 'UTF-8');
}

/**
 * redirige a una URL dada
 * @param string $url la URL a redirigir
 * @return void
 */

function redirect(string $path): void
{
    header("Location: $path");
    exit;
}

/**
 * valida los datos de una venta
 * @param array $data los datos a validar
 * @return array un array de errores, vacio si no hay errores
 */

function validateVenta(array $data): array
{
    $errors = [];

    // producto requerido, minimo 3 caracteres
    $producto = trim($data['producto'] ?? '');
    if ($producto === '' || mb_strlen($producto) < 3) {
        $errors['producto'] = 'El producto es requerido y debe tener al menos 3 caracteres';
    }

    // monto requerido, debe ser un numero positivo
    $monto = ($data['monto'] ?? '');
    if ($monto === '' || !is_numeric($monto) || $monto <= 0) {
        $errors['monto'] = 'El monto es requerido y debe ser un numero positivo';
    }

    // fecha requerida, debe ser una fecha valida
    $fecha = trim($data['fecha'] ?? '');
    $dt = DateTime::createFromFormat('Y-m-d', $fecha);
    $isValidDate = $dt && $dt->format('Y-m-d') === $fecha;

    if ($fecha === '' || !$isValidDate) {
        $errors['fecha'] = 'La fecha es requerida y debe ser una fecha valida (YYYY-MM-DD)';
    }

    return $errors;
}

