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
