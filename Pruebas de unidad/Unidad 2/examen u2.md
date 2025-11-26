- En la organización de eventos, es fundamental calcular correctamente la disposición del espacio para acomodar a todos los asistentes. Este programa ayuda a determinar cuántas filas de asientos se necesitan, teniendo en cuenta el número de asistentes y los asientos por fila. Además, genera un informe con la fecha y hora del evento, y recoge una valoración de satisfacción para calcular un número de control y un código de sesión.


- Primero se solicita al usuario el número de asistentes mediante prompt, y se convierte a número entero con parseInt:
```
var asistentes = parseInt(prompt("Introduce el número de asistentes: "));
```

- Se comprueba si el número de asistentes es menor o igual a 0. Si lo es, se muestra una alerta:
```
if (asistentes <= 0) {
    alert("Solo se pueden poner números enteros mayores que 0");
}
```

- Luego se solicita el número de asientos por fila, también convertido a entero:
```
var asientos_por_fila = parseInt(prompt("Introduce el número de asientos por fila: "));
```

- Se valida que el número de asientos por fila sea mayor que 0:
```
if (asientos_por_fila <= 0) {
    alert("Solo se pueden poner números enteros mayores que 0");
}
```

- Se pide la fecha del evento en formato AAAA-MM-DD HH:MM:
```
var fecha_evento = prompt("Introduce la fecha del evento en formato AAAA-MM-DD HH:MM");
```

- La cadena de fecha se convierte en un objeto Date: `var fecha = new Date(fecha_evento);`

- Se calcula el número de filas necesarias redondeando hacia arriba con Math.ceil:
```
var filas = Math.ceil(asistentes / asientos_por_fila);
``
```

- Se extraen los componentes de la fecha (año, mes, día, hora y minutos) usando métodos del objeto Date:
```
var año = fecha.getFullYear();
var mes = fecha.getMonth() + 1;  // Enero = 0
var día = fecha.getDate();
var horas = fecha.getHours();
var minutos = fecha.getMinutes();
```

- Se solicita al usuario tres niveles de satisfacción:
```
var satisfaccion1 = prompt("Introduce tu primer nivel de satisfacción: ");
var satisfaccion2 = prompt("Introduce tu segundo nivel de satisfacción: ");
var satisfaccion3 = prompt("Introduce tu tercer nivel de satisfacción: ");
```

- Se calcula la media de satisfacción:
```
var media = (satisfaccion1 + satisfaccion2 + satisfaccion3) / 3;
```

- Se genera un código de sesión usando el valor de π multiplicado por 100 y redondeado:
```
var codigo_sesion = Math.round(Math.PI * 100);
```

- Finalmente, se muestra un informe en pantalla con todos los datos:
```
document.write("=== Informe del Evento ===<br>");
document.write("Número de asistentes: ", asistentes, "<br>");
document.write("Asientos por fila: ", asientos_por_fila, "<br>");
document.write("Filas necesarias: ", filas, "<br>");
document.write("Fecha del evento: ");
document.write("Año: ", año, " Mes: ", mes, " Día: ", día, "<br>");
document.write("Hora: ", horas, " Minutos: ", minutos,  "<br>");
document.write("Número de control (media satisfacción ): ", media, "<br>");
document.write("Código de sesión: ", codigo_sesion, "<br>");
```



- A continuación se muestra un ejercicio que, gracias a cálculos, validaciones y condicionales, calcula el número de filas necesarias para un evento, muestra la fecha y hora del evento, y genera un número de control basado en la satisfacción del usuario:
```
<script>
/*
Programa calculador de filas
v0.1 Daniel Calve Pardo 2025
Este programa calcula cuantas filas necesitas para sentar a los asistentes de un evento, redondeando y mostrando un informa fecha/hora del evento
*/

// Pedir datos al usuario
var asistentes = parseInt(prompt("Introduce el numero de asistentes: "));
if (asistentes <= 0) {
    alert("Solo se pueden poner números enteros mayores que 0");
}

var asientos_por_fila = parseInt(prompt("Introduce el numero de asientos por fila: "));
if (asientos_por_fila <= 0) {
    alert("Solo se pueden poner números enteros mayores que 0");
}

var fecha_evento = prompt("Introduce la fecha del evento en formato AAAA-MM-DD HH:MM");


// Convertimos la cadena a un objeto Date
var fecha = new Date(fecha_evento);


// Calcular numero de filas necesarias 
var filas = Math.ceil(asistentes / asientos_por_fila);


// Mostrar informe de fecha
var año = fecha.getFullYear();
var mes = fecha.getMonth() + 1;  // Enero = 0
var día = fecha.getDate();
var horas = fecha.getHours();
var minutos = fecha.getMinutes();


// Pedimos el grado de satisfaccion
var satisfaccion1 = prompt("Introduce tu primer nivel de satisfaccion: ");
var satisfaccion2 = prompt("Introduce tu segundo nivel de satisfaccion: ");
var satisfaccion3 = prompt("Introduce tu tercer nivel de satisfaccion: ");

var media = (satisfaccion1*1 + satisfaccion2*1+ satisfaccion3*1)/3;
var codigo_sesion = Math.round(Math.PI * 100);  // Ejemplo usando PI


// Mostramos en pantalla
document.write("=== Informe del Evento ===<br>");
document.write("Número de asistentes: ", asistentes, "<br>");
document.write("Asientos por fila: ", asientos_por_fila, "<br>");
document.write("Filas necesarias: ", filas, "<br>");
document.write("Fecha del evento: ");
document.write("Año: ", año, " Mes: ", mes, " Día: ", día, "<br>");
document.write("Hora: ", horas, " Minutos: ", minutos,  "<br>");
document.write("Número de control (media satisfacción ): ", media, "<br>");
document.write("Código de sesión: ", codigo_sesion, "<br>");

</script>
```



- Este ejercicio muestra cómo utilizar JavaScript para recoger datos del usuario, realizar cálculos y generar un informe completo. Se aplican validaciones, operaciones matemáticas y manipulación de fechas. Además, se introduce una valoración subjetiva que se transforma en datos útiles para el control del evento