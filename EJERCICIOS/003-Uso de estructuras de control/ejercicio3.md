- En el mundo de las artes marciales mixtas (MMA), los combates se deciden por la habilidad, la estrategia y, a veces, un poco de suerte. En esta actividad, vamos a simular un combate entre dos luchadores utilizando JavaScript. El objetivo es practicar conceptos fundamentales de programación como funciones, estructuras de control (bucles y condicionales) y el retorno de valores. A través de esta simulación, aprenderás a estructurar una función que represente un combate, calcular puntos y determinar un ganador.


- Definir la función `calculaPuntos(jugador1, jugador2)`

- Esta función recibirá dos nombres de jugadores como parámetros. Dentro de ella, se simularán 5 rondas de combate.


- Inicializar los puntos de cada jugador. Se crean dos variables: `puntosJugador1` y `puntosJugador2`, ambas inicializadas a 0:
```
var puntosJugador1 = 0;
var puntosJugador2 = 0;
```

-Simular las rondas del combate
Se utiliza un bucle for que se repite 5 veces (una por cada ronda):
```
for (let ronda = 1; ronda <= 5; ronda++)
```

- Se genera un número aleatorio entre 0 y 10 para simular el ataque del jugador 1:
```
var ataqueJugador1 = Math.random() * 10;
```

Se genera otro número aleatorio entre 0 y 10 para simular la defensa del jugador 2:
```
var defensaJugador2 = Math.random() * 10;
```

- Si el ataque de jugador 1 es mayor que la defensa de jugador 2, jugador 1 gana 2 puntos. Si la defensa de jugador 2 es mayor, él gana 2 puntos:
```
if (ataqueJugador1 > defensaJugador2) {
      puntosJugador1 += 2;
    } else if (defensaJugador2 > ataqueJugador1) {
      puntosJugador2 += 2;
    }
```

- Si hay empate, nadie gana puntos.




- Al finalizar las rondas, se muestran los puntos obtenidos por cada jugador: 
```
console.log("Puntos " + jugador1 + ": " + puntosJugador1);
console.log("Puntos " + jugador2 + ": " + puntosJugador2);
```

- Y se declara al ganador o si hubo empate:
```
if (puntosJugador1 > puntosJugador2) {
    console.log(jugador1 + " gana el combate!");
  } else if (puntosJugador2 > puntosJugador1) {
    console.log(jugador2 + " gana el combate!");
  } else {
    console.log("Empate!");
  }
```

- Por ultimo, se prueba a la funcion, llamandola:
```
calculaPuntos("Jugador A", "Jugador B");
```

- A continuación se muestra un ejercicio que, gracias a cálculos y a condicionales, simula un combate de MMA entre dos jugadores, calcula los puntos obtenidos en cada ronda y determina al ganador:
```
<script>
/*
Programa simulador
v0.1 Daniel Calve Pardo 2025
Este programa simula una pelea de MMA
*/

function calculaPuntos(jugador1, jugador2) {
  var puntosJugador1 = 0;
  var puntosJugador2 = 0;

  for (let ronda = 1; ronda <= 5; ronda++) {
    var ataqueJugador1 = Math.random() * 10;
    var defensaJugador2 = Math.random() * 10;

    if (ataqueJugador1 > defensaJugador2) {
      puntosJugador1 += 2;
    } else if (defensaJugador2 > ataqueJugador1) {
      puntosJugador2 += 2;
    }
  }

  console.log("Puntos " + jugador1 + ": " + puntosJugador1);
  console.log("Puntos " + jugador2 + ": " + puntosJugador2);

  if (puntosJugador1 > puntosJugador2) {
    console.log(jugador1 + " gana el combate!");
  } else if (puntosJugador2 > puntosJugador1) {
    console.log(jugador2 + " gana el combate!");
  } else {
    console.log("Empate!");
  }
}
calculaPuntos("Jugador A", "Jugador B");
calculaPuntos("Jugador A", "Jugador B");
calculaPuntos("Jugador A", "Jugador B");
calculaPuntos("Jugador A", "Jugador B");
calculaPuntos("Jugador A", "Jugador B");
calculaPuntos("Jugador A", "Jugador B");


</script>
```

- Este ejercicio te ha permitido simular un combate de MMA utilizando JavaScript, aplicando funciones, bucles y condicionales. Has aprendido a generar valores aleatorios para representar acciones dinámicas, a comparar resultados y a mostrar información en consola. Este tipo de simulaciones no solo son divertidas, sino que también refuerzan tu lógica de programación y tu capacidad para estructurar código de forma clara y funcional.