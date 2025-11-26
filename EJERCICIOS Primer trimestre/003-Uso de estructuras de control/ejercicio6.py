# Programa media golpes
# v0.1 Daniel Calve Pardo 2025
#Este programa calcula la media de golpes recibidos en el total de combates


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
print(calcular_ratio_golpes(20, 5))   # Imprime 5.0
print(calcular_ratio_golpes(3, 0))   # Imprime "No se puede dividir por cero"
print(calcular_ratio_golpes("a", 12))  # Imprime "Los valores deben ser numéricos"
