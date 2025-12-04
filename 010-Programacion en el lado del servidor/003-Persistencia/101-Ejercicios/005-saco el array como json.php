<?php
  $cliente = [];
  $cliente['nombre'] = "Daniel";
  $cliente['apellidos'] = "Calve Pardo";
  $cliente['email'] = "dani@example.com";
  
  $json = json_encode($cliente);
  echo $json;  
?>