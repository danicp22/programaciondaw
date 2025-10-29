"""
Programa calculador de IMC
v0.1 Daniel Calve Pardo 2025
Este programa calcula el IMC de cada peleador a partir de sus datos de peso y altura
"""


class FitnessTracker:
    @staticmethod
    def calcularIMC(peso, altura):
        # Calcula el IMC usando la fórmula del enunciado
        return peso / (altura ** 2)


# Lista de participantes (nombre, peso en kg, altura en m)
participantes = [
    ("Tú", 70, 1.75),
    ("Gustavo", 60, 1.65),
    ("Andres", 80, 1.80),
    ("Zaka", 55, 1.60),
    ("Nico", 90, 1.85)
]

print("Cálculo de IMC")

# Calcular y mostrar el IMC de cada participante
for nombre, peso, altura in participantes:
    imc = FitnessTracker.calcularIMC(peso, altura)
    print(nombre, ": Peso = ",peso, "kg, Altura = ",altura, "m → IMC = ",imc)
