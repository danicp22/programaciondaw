- El objetivo de este ejercicio es aprender a manejar el objeto Date en JavaScript para obtener información sobre la fecha actual, como el año y el mes. Esta práctica permite familiarizarse con los métodos predefinidos del lenguaje y comprender cómo se pueden extraer datos temporales que son útiles en aplicaciones como calendarios, registros de eventos o seguimiento de actividades.


- Para comenzar, se crea la variable fechaActual, a la que se le añade `new Date()` para que genere la hora actual. 

Despues se crea la variable aniocompleto, y dentro se pone la primera variable junto con el metodo getFullYear, esto lo que hace es que nos dice el año actual:

`var anioCompleto = fechaActual.getFullYear();`

Despues se imprime en consola.

Y por ultimo hacemos lo mismo pero con el mes:

`var mesActual = fechaActual.getMonth() +1;`

Al mes se le suma 1 ya que los meses en JavaScript van del 0 al 11



- A continuacion se muestra un ejercicio que muestra en consola el año y mes actual:
```
<script>
/*Programa utilizacion de metodos
v0.1 Daniel Calve Pardo 2025
Este programa muestra la fecha actual
*/

//Crear una variable con la fecha actual
var fechaActual = new Date();

//Obtener el año completo
var anioCompleto = fechaActual.getFullYear();
console.log(anioCompleto); // Imprime el año actual

//Obtener el mes actual (0 = enero, 11 = diciembre)
var mesActual = fechaActual.getMonth() +1;
console.log(mesActual); // Imprime el mes actual

</script>
```


- En este ejercicio se ha aprendido a utilizar métodos predefinidos del objeto Date para extraer información de la fecha actual. Estos conocimientos son fundamentales en situaciones reales, como el seguimiento de eventos deportivos, la gestión de calendarios o cualquier aplicación que requiera registrar y mostrar fechas de manera precisa. Además, se refuerza la importancia de seguir convenciones de nomenclatura y de utilizar correctamente los métodos del lenguaje para obtener resultados fiables


