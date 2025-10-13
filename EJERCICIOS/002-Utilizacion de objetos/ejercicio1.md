- En este ejercicio, vamos a crear una clase Luchador en Python. El objetivo es simular un luchador que puede entrenar y pelear, aumentando o disminuyendo su energía. Podemos ver cómo los entrenamientos aumentan nuestra energía y la actividad de una pelea la reduce, igual que en la vida real.


- Creamos la clase Luchador con los atributos solicitados: nombre, edad, peso y energia, el constructor `__init__` inicializa estos atributos al crear un nuevo luchador:
```
class Luchador():   
    def __init__(self, nombre, edad, peso, energia):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.energia = energia
```
También agregamos los métodos entrenar() y pelear() para modificar la energía del luchador.
```def entrenar(self): 
        self.energia += 5
    
    def pelear(self): 
        self.energia -= 10
```
Despues creamos al luchador y le añadimos los datos que queramos:
`luchador1 = Luchador("Dani", 18, 76, 100)`

Y por ultimo llamamos al metodo entrenar, o pelear para que modifique la energia:
```
luchador1.entrenar()

luchador1.pelear()
```

- A continuacion se muestra un ejemplo practico, en el que la enegria del luchador sube 5 puntos cada vez que entrena y baja 10 cada vez que pelea:
```
#Programa registro de energia de luchador
#v0.1 Daniel Calve Pardo 2025
#Este programa muestra la energia que simula la energia de las peleas


class Luchador():   #Se define la clase y los atributos
    def __init__(self, nombre, edad, peso, energia):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.energia = energia

    def entrenar(self): #Se añade un metodo para aumentar la energia
        self.energia += 5
        print("Has entrenado. Energia actual: ",luchador1.energia)
    
    def pelear(self): #Se añade un metodo para disminuir la energia
        self.energia -= 10
        print("Estas peleando. Energia actual: ",luchador1.energia)

luchador1 = Luchador("Dani", 18, 76, 100) #Se crea el luchador
print("Energia inicial de",luchador1.nombre,":" ,luchador1.energia)

luchador1.entrenar()
luchador1.entrenar()
luchador1.entrenar()

luchador1.pelear()

print("Energia final: ",luchador1.energia)
```

- Este ejemplo permite entender cómo los objetos en programación representan entidades del mundo real.
Cada luchador es un objeto con atributos (nombre, edad, peso, energía) y comportamientos (entrenar, pelear).
Aplicando esto a los deportes de contacto, podemos simular rutinas de entrenamiento, desgaste por combates o estrategias para recuperar energía.
Así, aprendemos que la programación orientada a objetos ayuda a modelar situaciones reales, haciendo más fácil organizar información y acciones en un programa.