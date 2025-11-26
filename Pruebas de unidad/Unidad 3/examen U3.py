"""
Programa gestion de aforo y recaudacion
v0.1 Daniel Calve Pardo
Este programa gestiona el aforo de una sala y su recaudacion
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
            continue  # salto al siguiente intento
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
