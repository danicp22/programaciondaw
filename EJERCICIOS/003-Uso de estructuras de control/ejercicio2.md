- En aplicaciones web, es común generar contenido dinámico que se repite en función de ciertos parámetros, como fechas. Este ejemplo muestra cómo recorrer un rango de años, meses y días para imprimir todas las fechas posibles entre 1978 y 2025, usando bucles anidados. Es útil para entender cómo se estructuran ciclos en JavaScript y cómo se puede generar contenido repetitivo en una página web.



- Se declaran las variables que se usarán en los bucles:
```
var anio;
var mes;
var dia;
```


- Este bucle recorre los años desde 1978 hasta 2025:
`for (mes = 1; mes <= 12; mes++)`


- Dentro de cada año, se recorren los 12 meses:
`for (mes = 1; mes <= 12; mes++) {`


- Dentro de cada mes, se recorren los días del 1 al 30. (Nota: no se consideran meses con 31 días ni febrero con 28/29):
`for (dia = 1; dia <= 30; dia++) {`

- Se imprime la fecha en el documento HTML. El uso de document.write genera contenido directamente en la página:
```
document.write("Hoy es el día ", dia, " del mes ", mes, " del año ", anio, "<br>");
```



- A continuacion se muestra un ejercicio en el que se generan automaticamente fechas desde un año a otro, generando todos los dias y todos los meses de todos los años:
```
<script>

/*
Programa generador de fechas
v0.1 Daniel Calve Pardo 2025
Este programa genera gracias a bucles unas fechas
*/


// Declaración de variables
var anio;
var mes;
var dia;

// Bucle para los años
for (anio = 1978; anio <= 2025; anio++) {

    // Bucle para los meses
    for (mes = 1; mes <= 12; mes++) {

        // Bucle para los días (del 1 al 30)
        for (dia = 1; dia <= 30; dia++) {

            // Impresión de la fecha usando comas
            document.write("Hoy es el día ", dia, " del mes ", mes, " del año ", anio, "<br>");
        }
    }
}

</script>
```


- Este ejemplo muestra cómo usar bucles anidados para generar combinaciones de fechas. Aunque es funcional, tiene limitaciones: no considera la cantidad real de días por mes ni los años bisiestos. Como mejora, podrías usar objetos Date de JavaScript para manejar fechas reales, o limitar la impresión a fechas válidas. También podrías usar console.log en lugar de document.write si estás trabajando en un entorno de desarrollo.