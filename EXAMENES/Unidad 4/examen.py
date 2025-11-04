# Programa Desarrollo de clases
# v0.1 Daniel Calve Pardo 2025
# En este programa se crea una clase, se le añaden propiedades, metodos, constructores, instancias y se demuestra que todo funcione.


class Cliente():
    # Constructor con parametros
    def __init__(self,nombre,apellidos,email,telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        
        
    # Metodo set     
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
        
    # Metodo get
    def getEmail(self):
        return self.email
    
     
     
# Creamos tres instancias de la clase Cliente
cliente1 = Cliente("Daniel", "Calve Pardo", "dani@gmail.com", "657483932")
cliente2 = Cliente("Jorge", "Gomez Perez", "jorge@gmail.com", "678590499")
cliente3 = Cliente("Antonio", "Recio Matamoros", "mariscosrecio@gmail.com", "647567465")

# Mostramos los datos originales
print("Datos originales")
print(cliente1.getEmail())
print(cliente2.getEmail())
print(cliente3.getEmail())


# Modificamos los datos originales
cliente1.setEmail("cliente1@gmail.com")
cliente2.setEmail("cliente2@gmail.com")
cliente3.setEmail("cliente3@gmail.com")


# Mostramos los nuevos datos
print("Nuevos datos")
print(cliente1.getEmail())
print(cliente2.getEmail())
print(cliente3.getEmail())

