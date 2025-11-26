- En muchos programas, especialmente aquellos relacionados con entrenamiento, educación o progresión de habilidades, es útil clasificar a los usuarios según su nivel de experiencia. Este tipo de clasificación permite adaptar contenidos, entrenamientos o recomendaciones de forma más precisa. En este caso, se quiere determinar el nivel de una persona en función de sus años de entrenamiento.



- Se define una variable con el número de años que lleva entrenando una persona: `años_entrenamiento = 4`

- Si los años son menores que 5, se considera que la persona está en un nivel principiante:
```
if años_entrenamiento < 5:
    nivel = "Nivel principiante"
```

- Si no se cumple la condición anterior, pero los años son menores o iguales a 10, se clasifica como nivel intermedio:
```
elif años_entrenamiento <= 10:
    nivel = "Nivel intermedio"
```


- Si ninguna de las condiciones anteriores se cumple, se considera que la persona tiene un nivel avanzado:
```
else:
    nivel = "Nivel avanzado"
```

- Finalmente, se imprime el resultado con el número de años y el nivel correspondiente:
```
print("Años de entrenamiento: ", años_entrenamiento, "->", nivel)
```



- A continuacion se muestra un ejercicio que clasifica al peleador segun su tiempo de entrenamiento:
```
años_entrenamiento = 4  

# Clasificación sin estructuras anidadas
if años_entrenamiento < 5:
    nivel = "Nivel principiante"
elif años_entrenamiento <= 10:
    nivel = "Nivel intermedio"
else:
    nivel = "Nivel avanzado"

# Mostrar resultado
print("Años de entrenamiento: ",años_entrenamiento, "->", nivel)
```


- Este ejemplo muestra cómo usar condicionales simples para clasificar datos numéricos en categorías. Es una técnica muy útil en sistemas de recomendación, plataformas educativas o aplicaciones deportivas. Como mejora, podrías usar funciones para encapsular la lógica de clasificación o incluso estructuras más avanzadas como diccionarios si el rango de niveles se vuelve más complejo.


