<?php

require_once __DIR__ . '/db.php';
require_once __DIR__ . '/helpers.php';


if($_SERVER['REQUEST_METHOD'] !== 'POST'){
    redirect('index.php');
}

if(!isset($_POST['id'])  || !is_numeric($_POST['id'])){
    redirect('index.php');

}

$id = (int) $_POST['id'];

try{
    $pdo = getPDO();
    // se prepara la consulta SQL para eliminar la venta por id
    $stmt = $pdo->prepare("DELETE FROM ventas WHERE id = :id");
    // se ejecuta la consulta con el id de la venta a eliminar 
    $stmt ->execute(['id' => $id]);
    //redirigimos a index.phph despues de eliminar la venta 
    redirect('index.php');
    // El usos de consultas preparadas con pDO ayuda a prevenir inyecciones SQ
    // Ya que los parametros se manejan de forma se"gura

}catch (Throwable $e){
    // si ocurre un error, se ,muestra mensaje de error y se dirige a inde.php
    http_response_code(500);
    //htmlspecialchars() se utiliza para convertir caracteres 
    // especiales en entidades HTML, lo que ayuda a prevenoir ataques de Cross-Site
    // Scripting (XSS) al mostrar mensaje de error 
    echo "<h3> Error al eliminar la venta:</h3>";
    // El mensaje de error se muestra de forma segura
    // utilizando htmlspecialchars() para evitar posibles ataques XSS
    echo "<p>{$e->getMessage()}</p>";
    // se proporciona un enlace para volver a la pagina principal 
    // despues de mostrar el error 
    echo "<p> <a href='index.php'> Volver </a> </p>";


}