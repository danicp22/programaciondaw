- En el mundo de los videojuegos y la animación, los combates entre personajes con estilos de pelea distintos son muy comunes. Este ejercicio simula una pelea entre dos luchadores, mostrando sus nombres y estilos de combate. Aunque no se realiza una pelea real, se establece una estructura que podría ampliarse en versiones futuras del programa.




- Se define la clase `Pelea`, que representa un enfrentamiento entre dos luchadores.
- El método `__init__` es el constructor que recibe dos objetos de tipo `Gato`.
- `self.guerrero1` y `self.guerrero2` almacenan los luchadores que participan en la pelea.

```
class Pelea:
    def __init__(self, guerrero1: 'Gato', guerrero2: 'Gato'):
        self.guerrero1 = guerrero1
        self.guerrero2 = guerrero2
```

> Nota: Se usa `'Gato'` entre comillas como anotación de tipo para evitar errores si la clase `Gato` aún no está definida en ese momento.



- Se define la clase `Gato`, que representa a un luchador.
- El constructor recibe dos parámetros: `nombre` (nombre del luchador) y `estilo` (su estilo de pelea).
- Estos valores se guardan en los atributos `self.nombre` y `self.estilo`.

```
class Gato:
    def __init__(self, nombre, estilo):
        self.nombre = nombre
        self.estilo = estilo
```



- Se crean dos instancias de la clase `Gato`:
    - `g1` representa a Ryu, que pelea con estilo MMA.
    - `g2` representa a Ken, que pelea con estilo Boxeo.

```
g1 = Gato("Ryu", "MMA")
g2 = Gato("Ken", "Boxeo")
```




- Se crea una instancia de la clase `Pelea`, usando los dos luchadores creados anteriormente

```
pelea = Pelea(g1, g2)
```


- Se imprime la información de cada luchador accediendo a los atributos `nombre` y `estilo` desde el objeto `pelea`.

```
print("Guerrero 1:", pelea.guerrero1.nombre, "-", pelea.guerrero1.estilo)
print("Guerrero 2:", pelea.guerrero2.nombre, "-", pelea.guerrero2.estilo)
```





- A continuación se muestra un ejercicio que, gracias a clases e instancias, permite mostrar el nombre y el estilo de pelea de dos luchadores:

```
# Programa Simulador
# v0.1 Daniel Calve Pardo 2025
# Este programa muestra el nombre y el estilo de pelea de dos peleadores.

class Pelea:
    def __init__(self, guerrero1: 'Gato', guerrero2: 'Gato'):
        self.guerrero1 = guerrero1
        self.guerrero2 = guerrero2

class Gato:
    def __init__(self, nombre, estilo):
        self.nombre = nombre
        self.estilo = estilo

g1 = Gato("Ryu", "MMA")
g2 = Gato("Ken", "Boxeo")

pelea = Pelea(g1, g2)

print("Guerrero 1:", pelea.guerrero1.nombre, "-", pelea.guerrero1.estilo)
print("Guerrero 2:", pelea.guerrero2.nombre, "-", pelea.guerrero2.estilo)
```




- Este ejercicio introduce el uso de clases para modelar objetos con atributos específicos. Aunque el programa es sencillo, sienta las bases para futuras versiones que podrían incluir lógica de combate, estadísticas, y resultados. Se puede ampliar añadiendo métodos que simulen ataques, defensa o incluso una interfaz gráfica.

