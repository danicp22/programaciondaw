- En este ejercicio se desarrolla un programa que muestra información sobre una pelea de MMA. El objetivo es aplicar los conocimientos sobre el manejo de fechas y horas mediante el uso del objeto predeterminado `Date` del lenguaje JavaScript. El contexto del problema es simular un sistema que pueda registrar la fecha y hora exacta de una pelea, algo que resulta útil en sistemas de gestión de eventos deportivos, calendarios o aplicaciones que organizan competiciones.



- En este caso se ha utilizado el objeto `Date`, que permite crear, manipular y mostrar fechas y horas.

El programa crea una variable llamada `fechaPelea` con la fecha y hora de un evento deportivo específico,

`var fechaPelea = new Date(2025,10,12,11,30); `


y luego emplea los métodos getDate(), getMonth(), getFullYear(), getHours() y getMinutes() para obtener cada uno de los componentes de la fecha.
```
var dia = fechaPelea.getDate();
var mes = fechaPelea.getMonth();
var año = fechaPelea.getFullYear();
var hora = fechaPelea.getHours();
var minutos = fechaPelea.getMinutes();
```

Finalmente, los datos se formatean y se muestran en pantalla de forma legible, demostrando el uso correcto de los objetos nativos del lenguaje para trabajar con información temporal.

`console.log("La pelea comenzó el dia ",dia,"/",mes,"/",año, " a las ",hora,":",minutos);`




- A continuacion se muestra un ejercicio que utiliza el metodo date para mostrar en consola la hora y el dia de inicio de una pelea de MMA:
``` 
<script>
/*Programa informacion pelea
v0.1 Daniel Calve Pardo 2025
Este programa muestra informacion sobre una pelea de MMA
*/

//Creamos la variable y le asginamos los valores
var fechaPelea = new Date(2025,10,12,11,30); 

//Creamos una variable para cada valor y le asignamos el valor añadido antes
var dia = fechaPelea.getDate();
var mes = fechaPelea.getMonth();
var año = fechaPelea.getFullYear();
var hora = fechaPelea.getHours();
var minutos = fechaPelea.getMinutes();

//Mostramos en consola
console.log("La pelea comenzó el dia ",dia,"/",mes,"/",año, " a las ",hora,":",minutos);
</script>
```



- Este ejercicio permite comprender mejor cómo los objetos predeterminados del lenguaje facilitan la gestión de datos complejos como las fechas y horas.
La práctica está directamente relacionada con la unidad sobre manejo de objetos en JavaScript, ya que Date es un ejemplo claro de un objeto integrado con métodos y propiedades útiles para resolver problemas cotidianos en la programación.
En el futuro, este conocimiento puede aplicarse al desarrollo de aplicaciones web que gestionen eventos, reservas, horarios o recordatorios automáticos, mejorando la funcionalidad y precisión de los sistemas informáticos.