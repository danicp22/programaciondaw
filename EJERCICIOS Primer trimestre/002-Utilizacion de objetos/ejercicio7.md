- En la organización de eventos deportivos como las peleas de MMA, la gestión de fechas es fundamental. Los promotores, entrenadores y medios necesitan saber con precisión cuándo ocurrirá cada combate para coordinar logística, entrenamientos, publicidad y cobertura. Automatizar este proceso mediante programación permite reducir errores humanos y agilizar la planificación. Este tipo de scripts puede integrarse en sistemas más grandes de gestión de eventos deportivos.



- Primero creamos la variable `FechaPartido`a la que se le añade el metodo `new Date()` al cual le añadimos la fecha deseada: `var FechaPartido = new Date("2025-11-01");`

A continuacion se cambia la fecha que acabamos de añadir con el metodo `setDate()`, de esta manera: `FechaPartido.setDate(2);`

Despues se muestra por consola con el metodo `toString()`, este método convierte un objeto Date en una cadena legible: `console.log(FechaPartido.toString());`
 
Por ultimo se asigna `null` a `FechaPartido` para liberar su espacio de memoria: `FechaPartido = null;`





- A continuacion se muestra un ejercicio que muestra en consola la fecha de un combate de MMA, gracias a los metodos `new Date`, `setDate` y `toString`:

```
<script>
/*
Programa para gestionar peleas de MMA
v0.1 Daniel Calve Pardo 2025
Este programa muestra la fecha exacta del combate de MMA
*/

var FechaPartido = new Date("2025-11-01");

FechaPartido.setDate(2);

console.log(FechaPartido.toString());

FechaPartido = null;
</script>
```



- Este ejercicio demuestra cómo gestionar fechas de eventos deportivos con JavaScript. Aunque es simple, puede escalarse para incluir más funcionalidades como horarios, zonas horarias, recordatorios o integración con calendarios. Automatizar estos procesos mejora la eficiencia y reduce errores en la organización de combates de MMA.

