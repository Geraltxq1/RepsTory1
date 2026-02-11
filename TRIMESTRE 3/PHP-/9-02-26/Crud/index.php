<?php

/**
 * 
 * index.php
 * lista las ventas registradas en la base de datos
 * Incluye un enlace para agregar una nueva venta - editar y elminar.
 */

// Requerimos el archivo de conexión a la base de datos y 
//el archivo de funciones auxiliares

// EL PDO nos permite conectarnos a la base de datos 7
//y ejecutar consultas SQL manejo de errores y expcepciones.

require_once __DIR__ . '/db.php';
require_once __DIR__ . '/helpers.php';

$pdo = getPDO();

// Preparamos la consulta SQL para obtener todas las ventas

$stmt = $pdo->query("SELECT id, producto, monto,fecha,creado_en 
FROM ventas ORDER BY creado_en DESC");

$ventas = $stmt->fetchAll();

?>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Registro de ventas</title>

    <style>

        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }

        /*
            * .top es una clase CSS que se utiliza para crear un contenedor flexible
            * que alinea su contenido horizontalmente con espacio entre ellos y centra 
            * verticalmente los elementos dentro del contenedor. Además, se agrega un 
            * espacio de 12 píxeles entre los elementos utilizando la propiedad gap.
        */
        
        .top {
            display: flex; 
            justify-content: space-between;
            align-items: center; 
            gap: 12px;
        }

        .btn { 
            display: inline-block; 
            padding: 8px 12px; 
            border: 1px solid #333;
            text-decoration: none; 
            color: #111; 
            border-radius: 4px;
        }

        .btn:hover {
            background: #f2f2f2;
        }

    /*.
    .muted es una clase CSS que se utiliza para aplicar estilos a elementos de texto,
    como párrafos o etiquetas, para que se vean atenuados o menos destacados.
    form.inline es una clase CSS que se utiliza para aplicar estilos a un formulario 
    HTML,haciendo que se muestre en línea con otros elementos, en lugar de ocupar 
    toda la anchura disponible. Esto se logra estableciendo la propiedad display 
    en inline, lo que permite que el formulario se muestre junto a otros elementos 
    en lugar de ocupar una nueva línea.

    */
        .muted { 
            color: #666; 
            font-size: 0.9em;
        }

        form.inline { 
            display: inline; 
        }

        .danger { 
            border-color: #b00020; 
            color: #b00020;
        }

        .danger:hover { 
            background: #b00020; 
            color: #fff;
        }
       
        </style>
</head>

<body>

    <div class = "top">

        <div>

            <h1>Registro de ventas</h1>
            <p class="muted">Lista de ventas registradas en la base de datos</p>

        </div>

        <a  class="btn" href="create.php">Agregar venta</a>

    </div>
    
    <hr>

    <?php if (count($ventas) === 0): ?>

        <p>No hay ventas registradas.</p>

    <?php else: ?>

        <table>

        <thead>

                <tr>
                    <th>ID</th>
                    <th>Producto</th>
                    <th>Monto</th>
                    <th>Fecha</th>
                    <th>Creado en</th>
                    <th>Acciones</th>

                </tr>

        </thead>

        <tbody>

            <?php foreach ($ventas as $v): ?>

                <tr>

                    <td><?php echo $v['id']; ?></td>
                    <td><?php echo ($v['producto']); ?></td>
                    <td>$<?php echo number_format((float)$v['monto'], 2, ',', ','); ?>

                </td>

                    <td class="muted"><?php echo ($v['creado_en']); ?></td>

                    <td>

                        <a class="btn" href="edit.php?id=<?php echo (int)$v['id']; ?>">
                            Editar</a>
                        
            <!-- Eliminar por methodo POST para evitar que se eliminen borrados por url -->$_COOKIE

                    <form class="inline" method="POST" action="delete.php" 
                    onsubmit="return 
                    confirm('¿Estás seguro de eliminar esta venta?');">

                    <input type="hidden" name="id" value="<?php echo (int)$v['id'];
                     ?>">

                    <button type="submit" class="btn danger">Eliminar</button>

                    </form>

                    </td>

                </tr>

            <?php endforeach; ?>
    
        </tbody>

            </table>

            <?php endif; ?>

            <p  class ="muted" style=margin-top:18px>
            Si es la primera vez que ejecutas este proyecto, 
            asegúrate de ejecutar el script setup.php para crear la tabla.
            </p>

</body>

</html>
