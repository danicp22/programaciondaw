- En el mundo del MMA, los combates se organizan con precisión: cada pelea tiene dos luchadores, una categoría de peso, y una fecha programada. Para los aficionados que siguen cada evento, es útil registrar esta información de forma estructurada.
Los objetos en JavaScript permiten representar entidades reales como una pelea de MMA, agrupando sus características en una sola estructura. Además, el constructor Date() nos permite obtener la fecha actual del sistema, lo que es ideal para registrar cuándo se ha creado o programado una pelea.
En este ejercicio, usaremos un objeto literal para representar una pelea de MMA, y el constructor Date() para asignar la fecha actual. Esto nos permitirá modelar una situación real sin necesidad de clases personalizadas, aprovechando las herramientas nativas del lenguaje.



- Se crea un objeto literal llamado peleaMMA usando const, lo que significa que no se puede reasignar (aunque sus propiedades sí pueden cambiar): `const peleaMMA = { ... }`

- Se asigna el nombre, peso y categoria a los luchadores:
```
luchador1: {
        nombre: "Jon Jones",
        peso: 93,
        categoria: "heavyweight"
    },
    luchador2: {
        nombre: "Islam Makhachev",
        peso: 70.8,
        categoria: "welterweight"
    },

```

- Se usa el constructor Date() para obtener la fecha y hora actual del sistema. Esto se guarda como un objeto de tipo Date: `fecha: new Date()`




- A continuacion se muestra un ejercicio, que gracias a los objetos literales y los constructores, podemos mostrar en pantalla la informacion de una pelea de MMA:
```
<script>
    // Crear el objeto peleaMMA con luchadores y fecha
const peleaMMA = {
    luchador1: {
        nombre: "Jon Jones",
        peso: 93,
        categoria: "heavyweight"
    },
    luchador2: {
        nombre: "Islam Makhachev",
        peso: 70.8,
        categoria: "welterweight"
    },
    fecha: new Date()
};

// Mostrar la información de la pelea
document.write("Información de la pelea:<br><br>");
document.write(`Luchador 1: ${peleaMMA.luchador1.nombre}<br>`);
document.write(`Peso: ${peleaMMA.luchador1.peso} kg<br>`);
document.write(`Categoría: ${peleaMMA.luchador1.categoria}<br><br>`);


document.write(`Luchador 2: ${peleaMMA.luchador2.nombre}<br>`);
document.write(`Peso: ${peleaMMA.luchador2.peso} kg<br>`);
document.write(`Categoría: ${peleaMMA.luchador2.categoria}<br><br>`);


document.write(`Fecha de la pelea: ${peleaMMA.fecha.toLocaleString()}<br>`);

</script>
```





- Este ejercicio demuestra cómo los objetos en JavaScript permiten representar datos reales de forma estructurada. Usar Date() para asignar la fecha actual es útil en contextos dinámicos como el MMA, donde los eventos se programan constantemente.