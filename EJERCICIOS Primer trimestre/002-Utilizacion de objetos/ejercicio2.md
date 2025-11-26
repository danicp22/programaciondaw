- En este ejercicio se simula una situación deportiva: el registro del inicio de un combate y la puntuación obtenida por un jugador o equipo. El objetivo es practicar el uso de objetos predefinidos en JavaScript, en particular el objeto Date para manejar fechas y horas, y los métodos matemáticos para generar puntuaciones aleatorias. Esta simulación es útil para entender cómo se pueden registrar eventos deportivos en tiempo real o generar datos aleatorios para análisis.



- Para empezar se necesita crear la variable de la fecha actual, se utiliza esto:

`var fecha = new Date();`

A continuacion se crea la variable de la puntuacion, a la cual le hemos añadido el metodo `Math.random` para que genere un numero aleatorio, en este caso le he puesto para que sea del 0 al 10 y lo he multiplicado por 10 para que no me de solo numero 0,

`var puntuacion = Math.random(0,10) *10;`


Despues se crean las variables de la fecha (años,meses...), a estas variables tenemos que aplicarles el metodo get para que nos diga lo que le pidamos de manera exacta en este momento:
```
var anio = fecha.getFullYear();
var mes = fecha.getMonth();
var dia = fecha.getDate();
var hora = fecha.getHours();
var minutos = fecha.getMinutes();
var segundos = fecha.getSeconds();
```

Para finalizar imprimimos en consola 

```
console.log("La pelea empezo el dia:" ,dia,"/",mes,"/",anio," a las ",hora,":",minutos,":",segundos);
console.log("La puntuacion del combate es de: ",puntuacion, "puntos");
```




- A continuacion se muestra un ejercicio que muestra la puntucacion y la fecha del combate
```
<script>
/* Programa de registro de datos
v0.1 Daniel Calve Pardo 2025
Esre programa simula el tiempo en una situacion deportiva
*/

var fecha = new Date();
var puntuacion = Math.random(0,10) *10;

var anio = fecha.getFullYear();
var mes = fecha.getMonth();
var dia = fecha.getDate();
var hora = fecha.getHours();
var minutos = fecha.getMinutes();
var segundos = fecha.getSeconds();



console.log("La pelea empezo el dia:" ,dia,"/",mes,"/",anio," a las ",hora,":",minutos,":",segundos);
console.log("La puntuacion del combate es de: ",puntuacion, "puntos");

</script>
```


- En este ejercicio se ha aprendido a utilizar objetos y métodos predefinidos de JavaScript para manejar fechas y generar valores aleatorios. Estas habilidades son fundamentales en la programación de eventos deportivos, simulaciones o aplicaciones que requieren registro de tiempos y puntuaciones. La práctica permite comprender cómo automatizar el seguimiento de eventos y presentar información de manera estructurada y clara.

