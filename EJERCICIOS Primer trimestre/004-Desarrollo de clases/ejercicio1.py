# Programa Simulador
# v0.1 Daniel Calve Pardo 2025
# Este programa mestra el nombre y el estilo de pelea de dos peleadores.


# Definir la clase Pelea primero (usando 'Gato' entre comillas para la anotación de tipo)
class Pelea:
    def __init__(self, guerrero1: 'Gato', guerrero2: 'Gato'):
        # guerrero1 y guerrero2 serán objetos de tipo Gato
        self.guerrero1 = guerrero1
        self.guerrero2 = guerrero2


#Definir la clase Gato
class Gato:
    def __init__(self, nombre, estilo):
        self.nombre = nombre
        self.estilo = estilo


# Instanciar a los guerreros
g1 = Gato("Ryu", "MMA")
g2 = Gato("Ken", "Boxeo")


# Se crea una instancia de la pelea
pelea = Pelea(g1, g2)


#Imprimimos la informacion de la pelea
print("Guerrero 1:", pelea.guerrero1.nombre, "-", pelea.guerrero1.estilo)
print("Guerrero 2:", pelea.guerrero2.nombre, "-", pelea.guerrero2.estilo)