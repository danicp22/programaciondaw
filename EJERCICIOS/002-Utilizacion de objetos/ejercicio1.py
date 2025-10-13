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
    