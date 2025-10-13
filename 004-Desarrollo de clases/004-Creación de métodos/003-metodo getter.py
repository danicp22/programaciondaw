class Gato():
    def __init__(self):
        self.color = ""   #Esto es una propiedad

    def maulla(self):     #Esto es un metodo (es una accion)
        return "miau"

    def setColor(self,nuevocolor): #Defino un setter - el metodo es el responsable de cambiar la propiedad
        # Por ejemplo aqui podria validar si el color es un color valido para un gato
        self.color = nuevocolor     #Y cambio la propiedad

    def getColor(self):
        #Una vez mas aqui podria poner variaciones si lo quisiera
        return self.color 


gato1 = Gato()
gato1.color = "naranja"   #Aqui seteamos una propiedad directamente (no es buena practica)

gato1.setColor("naranja") #Esto es una practica mucho mejor

print(gato1.color)   #Acceso directo, se puede pero no se recomienda
 
print(gato1.getColor())  #Acceso mediante método, se recomienda