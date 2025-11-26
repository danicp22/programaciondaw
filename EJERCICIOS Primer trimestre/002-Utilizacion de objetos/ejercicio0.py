"""
Programa de torneo MMA 
Versión 0.1 por Daniel Calve Pardo
Este programa gestiona información sobre los participantes en un torneo de MMA.
"""

# No es necesario importar nada adicional


participantes = []
combates = []

class Participante:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

class Combate:
    def __init__(self, participante1, participante2):
        self.participante1 = participante1
        self.participante2 = participante2
        self.ganador = None


def principal():
    while True:
        print("1. Inscribir participante")
        print("2. Organizar combate")
        print("3. Mostrar resultados")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del participante: ")
            peso = float(input("Peso del participante (kg): "))
            participantes.append(Participante(nombre, peso))
            print("Participante inscrito con éxito.")
        elif opcion == "2":
            if len(participantes) < 2:
                print("No hay suficientes participantes para organizar un combate.")
            else:
                p1 = participantes.pop()
                p2 = participantes.pop()
                combate = Combate(p1, p2)
                combates.append(combate)
                print(f"Combate entre {p1.nombre} y {p2.nombre} organizado con éxito.")
        elif opcion == "3":
            for i, combate in enumerate(combates):
                print(f"Combate {i+1}: {combate.participante1.nombre} vs {combate.participante2.nombre}")
                ganador = input("Ganador: ")
                combate.ganador = ganador
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    principal()