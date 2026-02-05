<form method="GET">
<label> Ingrese un numero para ver su tabla</label>
<input type="numer" name= "numero"/>
<button type="submit">Enviar </button>
<form action="

</form>

<?php
if (isset($_GET["numero"])){
    $numero = (int) $_GET["numero"];

}else{
    $numero = 1;
}