Introducción y contextualización (25%):

- Para un entrenador de artes marciales mixtas , llevar un registro de las victorias del equipo es algo muy importante. De esta forma, puede analizar el rendimiento de los peleadores. En programación, podemos simular este registro utilizando operadores de incremento en JavaScript, que permiten aumentar valores de manera sencilla y precisa.

Desarrollo técnico correcto y preciso (25%):

- Primero se empieza creando la variable, a la cual le asignamos el valor:
`var partidas_ganadas = 0`
- Despues se añaden los operadores de incremento para aumentar esta valor:
`partidas_ganadas++;` 
    - En este caso he puedo 5 veces este comando para que sume 5 victorias, pero hay un punto en el que esto puede ser muy pesado y muy agotador, por lo cual se puede crear la estructura de control `if`, que lo que hace es reducir todo a un solo comando. 

Aplicación práctica con ejemplo claro (25%):
- A continuacion se muestra un ejercio sobre operaciones de incremento, en el que el programa lleva un registro sobre las victorias del equipo, en este caso solo aumentan.

'''
<script>
/*Programa registro de peleas ganadas
v0.1 Daniel Calve Pardo 2025
Este programa lleva un registro de las peleas ganadas por mi equipo
*/

//No hay librerias para importar

var partidas_ganadas = 0
   

// Simulamos 5 victorias (una llamada a ++ por victoria)
partidas_ganadas++; 
partidas_ganadas++; 
partidas_ganadas++; 
partidas_ganadas++; 
partidas_ganadas++;


// Imprimimos el resultado final
document.write("Partidas ganadas: ", partidas_ganadas); 

</script>

'''


Cierre/Conclusión enlazando con la unidad (25%):
- Este ejercicio demuestra cómo los operadores de incremento son una herramienta fundamental en JavaScript para manipular variables numéricas de forma rápida y clara. En el contexto de las MMA, los usamos para registrar victorias, pero en la vida real pueden aplicarse en muchos otros escenarios: contar puntos, registrar asistentes a un evento, o simplemente llevar la cuenta de intentos en un programa. Comprender cómo funcionan los operadores y expresiones nos permite automatizar procesos repetitivos con facilidad, uniendo la lógica de la programación con la organización de datos reales.
