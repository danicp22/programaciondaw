- En el boxeo profesional, llevar un control estadístico de los golpes recibidos por combate puede ser útil para analizar el rendimiento defensivo de un púgil. Este pequeño programa permite calcular la media de golpes recibidos por combate, lo que puede ayudar a entrenadores y analistas a evaluar si un boxeador está mejorando su defensa con el tiempo.



- El programa se basa en una función llamada `calcular_ratio_golpes`, que recibe dos parámetros:

   `golpes_recibidos`: número total de golpes que ha recibido el boxeador.
   `combates_total`: número total de combates disputados.



- Se intenta convertir ambos valores a enteros usando `int()`. Si alguno no es numérico, se captura el error con `try-except` y se devuelve un mensaje:
```
try:
        golpes_recibidos = int(golpes_recibidos)
        combates_total = int(combates_total)
    except ValueError:
        return "Los valores deben ser numéricos"
```

- Se verifica si el número de combates es cero para evitar una división por cero:
```
if combates_total == 0:
        return "No se puede dividir por cero"
```


- Si todo es correcto, se calcula el ratio dividiendo los golpes recibidos entre los combates:
```
    ratio = golpes_recibidos / combates_total
    return ratio
```


- Se comprueba:
```
print(calcular_ratio_golpes(20, 5))   # Imprime 5.0
print(calcular_ratio_golpes(3, 0))   # Imprime "No se puede dividir por cero"
print(calcular_ratio_golpes("a", 12))  # Imprime "Los valores deben ser numéricos"
```




- A continuación se muestra un ejercicio que, gracias a condicionales y manejo de errores, calcula la media de golpes recibidos por combate. También incluye validaciones para evitar errores comunes como introducir letras o dividir por cero.

```
# Programa media golpes
# v0.1 Daniel Calve Pardo 2025
# Este programa calcula la media de golpes recibidos en el total de combates

def calcular_ratio_golpes(golpes_recibidos, combates_total):
    # Intentamos convertir los valores a enteros
    try:
        golpes_recibidos = int(golpes_recibidos)
        combates_total = int(combates_total)
    except ValueError:
        return "Los valores deben ser numéricos"
    
    # Verificamos si el divisor es cero
    if combates_total == 0:
        return "No se puede dividir por cero"
    
    # Realizamos la división
    ratio = golpes_recibidos / combates_total
    return ratio

# Ejemplos de uso:
print(calcular_ratio_golpes(20, 5))      # Imprime 5.0
print(calcular_ratio_golpes(3, 0))       # Imprime "No se puede dividir por cero"
print(calcular_ratio_golpes("a", 12))    # Imprime "Los valores deben ser numéricos"
```



- Este programa es útil para calcular estadísticas básicas en deportes de contacto como el boxeo. Además de ser sencillo, incluye validaciones que lo hacen robusto frente a errores comunes. Se podría ampliar para incluir más métricas, como golpes dados, porcentaje de acierto, o evolución por temporada.


