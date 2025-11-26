- En el mundo del boxeo profesional, es fundamental que los deportistas tengan al menos 18 años para poder competir legalmente. Este pequeño programa en Python permite comprobar si un boxeador cumple con ese requisito de edad, utilizando una aserción para validar la condición.



- La función `comprobar_edad(edad)` realiza lo siguiente:

    1.  Entrada: recibe un parámetro `edad`.
    2.  Aserción: se usa `assert edad >= 18` para verificar que la edad sea válida.
        *   Si la condición se cumple, el programa continúa.
        *   Si no se cumple, lanza una excepción `AssertionError`.
    3.  Manejo de errores: se captura el error con `except AssertionError as e` y se muestra un mensaje personalizado.
    4.  Salida se imprime un mensaje indicando si el acceso está permitido o si hay un error.




- A continuación se muestra un ejercicio que, gracias a cálculos y condicionales, verifica si un boxeador tiene la edad mínima para competir:

```
# Definimos una función para comprobar la edad de un boxeador
def comprobar_edad(edad):
    try:
        # Aserción: la edad debe ser mayor o igual a 18
        assert edad >= 18, "El boxeador debe tener al menos 18 años."
        # Si la aserción pasa, informamos que está bien
        print(f"Edad {edad}: Acceso permitido — el boxeador es mayor de edad.")
    except AssertionError as e:
        # Si la aserción falla, capturamos el error y mostramos mensaje
        print(f"Edad {edad}: Error — {e}")

# Ejemplos
comprobar_edad(16)  # ejemplo que falla la aserción
comprobar_edad(21)  # ejemplo que pasa la aserción
```


- Este programa es útil para validar rápidamente si un boxeador cumple con el requisito de edad mínima. El uso de `assert` permite una verificación clara y directa, y el manejo de errores asegura que el usuario reciba un mensaje explicativo si la condición no se cumple.
