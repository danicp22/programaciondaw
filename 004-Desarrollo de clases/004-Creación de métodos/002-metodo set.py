class Gato():
    def __init__(self):
        self.color = 22   #Esto es una propiedad

    def maulla(self):     #Esto es un metodo (es una accion)
        return "miau"

    def setColor(self,nuevocolor): #Defino un setter - el metodo es el responsable de cambiar la propiedad
        # Por ejemplo aqui podria validar si el color es un color valido para un gato
        self.color = nuevocolor     #Y cambio la propiedad


gato1 = Gato()
gato1.color = "naranja"   #Aqui seteamos una propiedad directamente (no es buena practica)

gato1.setColor("naranja") #Esto es una practica mucho mejor