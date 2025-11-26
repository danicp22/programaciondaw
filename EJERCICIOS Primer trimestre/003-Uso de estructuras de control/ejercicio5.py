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
