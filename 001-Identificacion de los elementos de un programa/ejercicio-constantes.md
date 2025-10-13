Rúbrica de evaluación

1.Introducción y contextualización (25%):


- En el mundo de la programación, una constante en JavaScript es una variable cuyo valor no puede cambiar después de haber sido asignado. Se declara usando la palabra clave const. Sirve para asegurar que ciertos valores en tu código permanezcan fijos y no se modifiquen accidentalmente, lo que hace el código más predecible, seguro y fácil de mantener.




2.Desarrollo técnico correcto y preciso (25%):


- La constante se crea poniendo el comando `const` seguido del nombre que le queramos dar a la constante, despues del nombre, se le añade el valor que queremos asignarle, de la siguiente manera:

 ```
 const Peso_Maximo_Oponente = 200;
 ```

 - Despues se le intenta añadir otro valor a la constante:

 ``` 
 Peso_Maximo_Oponente = 150;
 ```
 - Esto lo que genera es un fallo, ya que ya se ha declarado un valor para una constante, por lo cual no se puede cambiar a no ser que crees otro valor para otra constante




3.Aplicación práctica con ejemplo claro (25%)



- Y a continuación se muestra un ejercico en el que se crea una constante, despues, esa constante se intenta cambiar dandole otro valor, lo que hace que de fallo:

```
<script>
    const Peso_Maximo_Oponente = 200; //Es importante declarar la constanste si queremos tener un variable que no cambia su valor
    Peso_Maximo_Oponente = 150; //Si ya tenemos asignada una constante y le intentamos dar otro valor, obviamente va a salir error
    console.log (Peso_Maximo_Oponente);
</script>

```





4.Cierre/Conclusión enlazando con la unidad (25%):   


En el desarrollo de aplicaciones para el entrenamiento de MMA, declarar valores como constantes inmutables es fundamental para garantizar la integridad y coherencia de los datos a lo largo del código. Al usar `const` en JavaScript, evitamos modificaciones accidentales que podrían causar errores o comportamientos inesperados en la aplicación, especialmente en valores críticos como límites de peso. Esto no solo mejora la seguridad y estabilidad del programa, sino que también facilita su mantenimiento y comprensión por parte de otros desarrolladores. En resumen, el uso adecuado de constantes fortalece la calidad del código y es una buena práctica esencial en cualquier proyecto de programación, contribuyendo a la creación de aplicaciones más robustas y confiables.