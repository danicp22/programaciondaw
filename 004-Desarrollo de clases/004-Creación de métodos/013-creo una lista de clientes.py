class Cliente():
    #Este es el metodo constructor
    def __init__(self):
        self.nombrecompleto = ""
        self.email = ""
    #Estos son los setters y los getters
    def setNombreCompleto(self.nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompletoç
    def getEmail(self):
        return self.email
# CRUD - Create, Read, Update, Delete
#CRUD SQL - INSERT, SELECT, UPDATE, DELETE

clientes =[]    ############# Meto una lista vacia


print("Gestos de clientes v0.1 Daniel Calve")
print("Selecciona una opcion")
print("1.- Insertar un nuevo cliente")
print("2.- Obteber listado de clientes")
opcion = int(input("Indica tu opcion (1,2):"))

if opcion == 1:
    print("Voy a insertar un cliente")
    nuevocliente = Cliente()
    nombrecliente = input("Introduce el nombre del cliente: ") #Tomo el dato
    nuevocliente.setNombreCompleto(nombrecliente) #Uso el metodo se para meter el dato en el objeto
    emailcliente = input("Introducre el email del cliente: ") #Tomo el dato
    nuevocliente.setEmail(emailcliente) #Uso el metodo se para meter el dato en el objeto
elif opcion == 2:
    print("Saco el listado de clientes")