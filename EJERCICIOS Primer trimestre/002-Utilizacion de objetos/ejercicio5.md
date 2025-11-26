- En el ámbito del fitness y la salud, el Índice de Masa Corporal (IMC) es una medida ampliamente utilizada para evaluar si una persona tiene un peso adecuado en relación con su altura. Aunque no es un indicador absoluto de salud, el IMC permite hacer una primera aproximación sobre posibles riesgos asociados al sobrepeso o la delgadez. Automatizar su cálculo mediante programación es útil en aplicaciones deportivas, clínicas, o incluso en gimnasios para hacer seguimientos personalizados.



- Primero se define una clase llamada `FitnessTracker`, que agrupa funcionalidades relacionadas con el seguimiento físico.

- Dentro de la clase, se crea un método estático llamado calcularIMC, que recibe dos parámetros: peso y altura. Al ser estático, se puede usar sin crear una instancia de la clase:
```
class FitnessTracker:
    @staticmethod
    def calcularIMC(peso, altura):
        return peso / (altura ** 2)
```

- A continuación, se crea una lista llamada participantes, que contiene tuplas con el nombre, peso (en kg) y altura (en metros) de cada persona:
```
participantes = [
    ("Tú", 70, 1.75),
    ("Gustavo", 60, 1.65),
    ("Andres", 80, 1.80),
    ("Zaka", 55, 1.60),
    ("Nico", 90, 1.85)
]
```

- Se imprime un encabezado para indicar que se va a calcular el IMC: `print("Calculo de IMC")`


- Luego se recorre la lista de participantes con un bucle for. En cada iteración se extraen el nombre, peso y altura, se calcula el IMC usando el método calcularIMC, y se muestra el resultado por consola:
```
for nombre, peso, altura in participantes:
    imc = FitnessTracker.calcularIMC(peso, altura)
    print(nombre, ": Peso = ", peso, "kg, Altura = ", altura, "m → IMC = ", round(imc, 2))
```


- A continuacion se muestra un ejercicio que muestra informacion sobre la altura y el peso de diferentes peleadores, este programa calcula el IMC de cada peleador a partir de los datos de peso y altura: 

```
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
```



- Este ejercicio muestra cómo aplicar programación orientada a objetos para resolver un problema práctico del mundo del fitness. El uso de métodos estáticos permite organizar el código de forma clara y reutilizable. Además, trabajar con listas de participantes facilita la escalabilidad del sistema. Este tipo de lógica puede integrarse fácilmente en aplicaciones móviles o plataformas web para ayudar a los usuarios a monitorear su salud.