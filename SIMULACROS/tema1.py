# Ticket de tienda básico
IVA = 0.21  # IVA del 21%

# Pedir datos al usuario
cliente_nombre = input("Nombre del cliente: ")
edad = int(input("Edad del cliente: "))

if edad < 18:
    print("No se puede emitir factura a menores de edad.")
else:
    base_imponible = float(input("Base imponible (€): "))

    # Calcular descuento
    if base_imponible < 100:
        descuento = 0
    elif base_imponible < 200:
        descuento = 5
    else:
        descuento = 10

    # Cálculos
    importe_descuento = base_imponible * descuento / 100
    base_tras_descuento = base_imponible - importe_descuento
    importe_iva = base_tras_descuento * IVA
    total = base_tras_descuento + importe_iva

    # Imprimir ticket
    print("--- TICKET DE TIENDA ---")
    print("Cliente:", cliente_nombre)
    print("Edad:", edad)
    print("Base imponible:", base_imponible, "€")
    print("Descuento:", descuento, "%")
    print("Importe descuento:", importe_descuento, "€")
    print("Base tras descuento:", base_tras_descuento, "€")
    print("IVA (21%):", importe_iva, "€")
    print("TOTAL A PAGAR:", total, "€")


