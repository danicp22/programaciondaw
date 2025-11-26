- En la gestión de eventos con aforo limitado, es fundamental controlar la venta de entradas y calcular la recaudación total. Este programa simula una taquilla digital que permite vender entradas hasta completar el aforo, validando cada operación, ajustando ventas si se supera el límite, y mostrando un resumen final con el total de entradas vendidas y el dinero recaudado.

- Se solicita el aforo total mediante un bucle `while` que valida que el valor sea un número entero positivo:
```
while True:
    try:
        aforo_total = int(input("Introduce el aforo total: "))
        if aforo_total <= 0:
            print("Debe ser un número mayor que 0.")
            continue
        break
    except ValueError:
        print("Error: debes introducir un número entero.")
```


- Se solicita el precio de la entrada, también validando que sea un número positivo (puede ser decimal):
```
while True:
    try:
        precio = float(input("Introduce el precio de la entrada: "))
        if precio <= 0:
            print("Debe ser un número mayor que 0.")
            continue
        break
    except ValueError:
        print("Error: debes introducir un número válido.")
```


- Se inicializan las variables que controlarán el estado de la taquilla:
```
aforo_restante = aforo_total
entradas_vendidas = 0
recaudacion = 0.0
ventas_efectivas = 0  # solo cuenta ventas válidas
```

-Se inicia el bucle de venta de entradas, que se ejecuta mientras haya aforo disponible:
```
while aforo_restante > 0:
```

- Dentro del bucle, se solicita cuántas entradas quiere comprar el usuario, validando que sea un número entero positivo:
```
    try:
        cantidad = int(input(f"¿Cuántas entradas quieres comprar? (restan {aforo_restante}): "))
        if cantidad <= 0:
            print("Solo se permiten números enteros positivos.")
            continue
    except ValueError:
        print("Entrada inválida. Debes introducir un número entero.")
        continue
```

- Se controla el aforo, y si el usuario pide más entradas de las disponibles, se le ofrece ajustar la compra:
```
    if cantidad > aforo_restante:
        ajustar = input(f"Sólo quedan {aforo_restante} entradas. ¿Quieres comprar esa cantidad? (S/N): ").strip().upper()
        if ajustar == "S":
            cantidad = aforo_restante
        else:
            print("Venta cancelada.")
            continue
```

- Se registra la venta, actualizando las variables correspondientes:
```
    entradas_vendidas += cantidad
    aforo_restante -= cantidad
    recaudacion += cantidad * precio
    ventas_efectivas += 1
```

- Se incluyen aserciones para garantizar que el estado del sistema es coherente:
```
    assert aforo_restante >= 0, "Error: aforo negativo"
    assert entradas_vendidas + aforo_restante == aforo_total, "Error: conservación de entradas"
```

- Cada 5 ventas efectivas, se muestra un mensaje de descanso técnico:
```
    if ventas_efectivas % 5 == 0:
        print("descanso técnico")
```

- Si el aforo se agota, se informa al usuario y se termina el bucle:
```
    if aforo_restante == 0:
        print("La sala está llena. No se pueden vender más entradas.")
        break
```

- Al final, se muestra un resumen con las entradas vendidas, la recaudación total y el estado del aforo:
```
print("\n=== Resumen de la Taquilla ===")
print(f"Entradas vendidas: {entradas_vendidas}")
print(f"Recaudación total: {recaudacion:.2f} €")
if aforo_restante == 0:
    print("Sala llena")
else:
    print(f"Quedan {aforo_restante} asientos disponibles")
```



- A continuación se muestra un ejercicio que, mediante bucles, condicionales, validaciones y cálculos, gestiona la venta de entradas en una sala con aforo limitado y calcula la recaudación total:

```
"""
Programa gestión de aforo y recaudación
v0.1 Daniel Calve Pardo
Este programa gestiona el aforo de una sala y su recaudación
"""

# Pedir datos iniciales
while True:
    try:
        aforo_total = int(input("Introduce el aforo total: "))
        if aforo_total <= 0:
            print("Debe ser un número mayor que 0.")
            continue
        break
    except ValueError:
        print("Error: debes introducir un número entero.")

while True:
    try:
        precio = float(input("Introduce el precio de la entrada: "))
        if precio <= 0:
            print("Debe ser un número mayor que 0.")
            continue
        break
    except ValueError:
        print("Error: debes introducir un número válido.")

# Inicialización de variables
aforo_restante = aforo_total
entradas_vendidas = 0
recaudacion = 0.0
ventas_efectivas = 0  # solo cuenta ventas válidas

# Bucle de venta de entradas
while aforo_restante > 0:
    try:
        cantidad = int(input(f"¿Cuántas entradas quieres comprar? (restan {aforo_restante}): "))
        if cantidad <= 0:
            print("Solo se permiten números enteros positivos.")
            continue
    except ValueError:
        print("Entrada inválida. Debes introducir un número entero.")
        continue

    # Control de aforo
    if cantidad > aforo_restante:
        ajustar = input(f"Sólo quedan {aforo_restante} entradas. ¿Quieres comprar esa cantidad? (S/N): ").strip().upper()
        if ajustar == "S":
            cantidad = aforo_restante
        else:
            print("Venta cancelada.")
            continue

    # Registrar venta
    entradas_vendidas += cantidad
    aforo_restante -= cantidad
    recaudacion += cantidad * precio
    ventas_efectivas += 1

    # Aserciones para invariantes
    assert aforo_restante >= 0, "Error: aforo negativo"
    assert entradas_vendidas + aforo_restante == aforo_total, "Error: conservación de entradas"

    # Descanso técnico cada 5 ventas efectivas
    if ventas_efectivas % 5 == 0:
        print("descanso técnico")
    
    # Sala llena
    if aforo_restante == 0:
        print("La sala está llena. No se pueden vender más entradas.")
        break

# Resumen final
print("\n=== Resumen de la Taquilla ===")
print(f"Entradas vendidas: {entradas_vendidas}")
print(f"Recaudación total: {recaudacion:.2f} €")
if aforo_restante == 0:
    print("Sala llena")
else:
    print(f"Quedan {aforo_restante} asientos disponibles")
```



- Este ejercicio muestra cómo gestionar el aforo de una sala de forma segura y eficiente, validando entradas, ajustando ventas y calculando la recaudación. Se aplican técnicas de control de flujo, validación de datos, uso de aserciones y lógica condicional. Como mejora, se podría añadir persistencia de datos o una interfaz gráfica para facilitar su uso en entornos reales.
