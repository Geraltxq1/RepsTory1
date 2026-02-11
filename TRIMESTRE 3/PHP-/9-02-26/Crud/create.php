<?php

/**
 * Formulario para crear una nueva venta
 */

require_once __DIR__ . '/helpers.php';

// valores por defecto para el formulario

$old = [
    'producto' => '',
    'monto' => '',
    'fecha' => '',
];

$errors = [];

// si hay errores en la query string, los decodificamos

if (isset($_GET['errors'])) {
    $errors = json_decode(base64_decode($_GET['errors']), true) ?? [];
}


if (isset($_GET['old'])) {
    $old = json_decode(base64_decode($_GET['old']), true) ?? $old;
}

?>


<!doctype html>
<html lang="es">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Nueva venta</title>

  <style>

    body { 
        font-family: Arial, sans-serif; 
        margin: 24px; 
    }

    label { 
        display:block; 
        margin-top: 10px; 
    }

    input { 
        width: 360px; 
        max-width: 100%; 
        padding: 8px; 
    }

    .btn { 
        display: inline-block; 
        padding: 8px 12px; 
        border: 1px solid #333; 
        text-decoration: none; 
        color: #111; 
        border-radius: 6px; 
        margin-top: 14px; 
    }

    .btn:hover { 
        background: #f2f2f2; 
    }

    .error { 
        color: #b00020; 
        margin: 6px 0 0; 
    }

    .muted { 
        color: #666; 
    }

  </style>
  
</head>

<body>

  <h1>Nueva venta</h1>

  <p class="muted">Completa el formulario y guarda.</p>

  <p><a class="btn" href="index.php">← Volver</a></p>

  <form method="POST" action="store.php">

    <label>Producto</label>

    <input type="text" name="producto" value="<?php echo h($old['producto']); ?>" placeholder="Ej: Teclado">

    <?php if (isset($errors['producto'])): ?>

      <p class="error"><?php echo h($errors['producto']); ?></p>

    <?php endif; ?>

    <label>Monto</label>

    <input type="number" step="0.01" name="monto" value="<?php echo h((string)$old['monto']); ?>" placeholder="Ej: 35000">

    <?php if (isset($errors['monto'])): ?>

      <p class="error"><?php echo h($errors['monto']); ?></p>

    <?php endif; ?>

    <label>Fecha</label>

    <input type="date" name="fecha" value="<?php echo h($old['fecha']); ?>">

    <?php if (isset($errors['fecha'])): ?>

      <p class="error"><?php echo h($errors['fecha']); ?></p>

    <?php endif; ?>

    <button class="btn" type="submit">Guardar</button>
    
  </form>

</body>

</html>