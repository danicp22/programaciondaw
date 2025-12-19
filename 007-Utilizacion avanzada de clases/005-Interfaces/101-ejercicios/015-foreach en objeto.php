<?php
	
  $cliente = [
  	"nombre" => "Daniel",
    "apellidos" => "Calve Pardo",
    "email" => "dani@example.com"
  ];

  foreach($cliente as $clave=>$valor){
    echo $clave. ": ".$valor."<br>";
  }

?>