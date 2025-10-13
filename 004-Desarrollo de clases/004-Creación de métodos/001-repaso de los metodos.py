class Gato():
    def __init__(self):
        self.color = 22   #Esto es una propiedad

    def maulla(self):     #Esto es un metodo (es una accion)
        return "miau"



gato1 = Gato()
gato1.color = "naranja"   #Aqui seteamos una propiedad
print(gato1.maulla())     #Aqui llamamos a un metodo
