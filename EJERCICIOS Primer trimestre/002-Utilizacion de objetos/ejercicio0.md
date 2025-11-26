- Para organizar un torneo de artes marciales mixtas (MMA), es fundamental llevar un control de los participantes, los combates y los resultados. En programación, podemos simular este proceso utilizando clases, listas y estructuras de control como condicionales y bucles. Esto nos permite automatizar tareas repetitivas y gestionar la información de forma ordenada.






Variables principales

```python
participantes = []
combates = []
```

- `participantes`: es una lista vacía que se irá llenando con objetos de tipo `Participante` a medida que se inscriban nuevos luchadores.
- `combates`: otra lista vacía que almacenará los combates organizados, cada uno representado por un objeto de la clase `Combate`.


Clases

Clase Participante

```python
class Participante:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
```

- Esta clase representa a un luchador.
- Tiene dos atributos:
  - `nombre`: el nombre del participante.
  - `peso`: el peso del participante, que podría usarse más adelante para clasificar por categorías (peso pluma, ligero, pesado, etc.).

Clase Combate

```python
class Combate:
    def __init__(self, participante1, participante2):
        self.participante1 = participante1
        self.participante2 = participante2
        self.ganador = None
```

- Esta clase representa un combate entre dos luchadores.
- Tiene tres atributos:
  - `participante1` y `participante2`: los dos luchadores que se enfrentan.
  - `ganador`: inicialmente es `None`, pero luego se actualiza con el nombre del ganador del combate.

---

Función principal

La función `principal()` es el núcleo del programa. Contiene un bucle `while True` que muestra un menú con opciones para el usuario. Este menú permite interactuar con el sistema de forma sencilla.

```python
def principal():
    while True:
        print("1. Inscribir participante")
        print("2. Organizar combate")
        print("3. Mostrar resultados")
        print("4. Salir")
        opcion = input("Elige una opción: ")
```

Opción 1: Inscribir participante

```python
if opcion == "1":
    nombre = input("Nombre del participante: ")
    peso = float(input("Peso del participante (kg): "))
    participantes.append(Participante(nombre, peso))
    print("Participante inscrito con éxito.")
```

- Se pide al usuario el nombre y el peso del luchador.
- Se crea un nuevo objeto `Participante` y se añade a la lista `participantes`.
- Esto permite ir construyendo la lista de luchadores disponibles para competir.

Opción 2: Organizar combate

```python
elif opcion == "2":
    if len(participantes) < 2:
        print("No hay suficientes participantes para organizar un combate.")
    else:
        p1 = participantes.pop()
        p2 = participantes.pop()
        combate = Combate(p1, p2)
        combates.append(combate)
        print(f"Combate entre {p1.nombre} y {p2.nombre} organizado con éxito.")
```

- Se verifica que haya al menos dos participantes disponibles.
- Se sacan los dos últimos inscritos (con `pop()`) para enfrentarlos.
- Se crea un nuevo objeto `Combate` y se añade a la lista `combates`.
- Se informa al usuario del combate organizado.


 Mostrar resultados

```python
elif opcion == "3":
    for i, combate in enumerate(combates):
        print(f"Combate {i+1}: {combate.participante1.nombre} vs {combate.participante2.nombre}")
        ganador = input("Ganador: ")
        combate.ganador = ganador
```

- Se recorren todos los combates organizados.
- Se muestra quiénes pelearon en cada uno.
- El usuario introduce el nombre del ganador, que se guarda en el atributo `ganador` del combate correspondiente.

Opción 4

```python
elif opcion == "4":
    break
```

Finaliza el programa



- A contuniacion se muestra un ejercicio que muestra un torneo de MMA, el cual inscribe a los peleadores, organiza el combate y muestra resultados:
```
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
```


- Este ejercicio demuestra cómo se pueden aplicar los conceptos básicos de la programación estructurada y orientada a objetos en Python para resolver un problema real. En este caso, se ha creado un sistema que permite gestionar un torneo de MMA, desde la inscripción de los participantes hasta la organización de combates y el registro de resultados.


Gracias al uso de clases, listas y estructuras de control, el programa es fácil de entender, mantener y ampliar. Por ejemplo, se podrían añadir nuevas funciones como mostrar estadísticas de cada luchador, registrar derrotas o empates, o incluso guardar los datos en un archivo para su análisis posterior.



