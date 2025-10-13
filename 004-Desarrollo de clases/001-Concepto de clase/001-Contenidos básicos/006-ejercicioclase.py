#CRUD
#Create
#Read
#Update
#Delete

class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

print("Programa de gestion de clientes v0.1 Daniel Calve Pardo")

print("Selecciona una opcion: ")
print("1.- Insertar un cliente")
print("2.- Listar clientes")
print("3.- Actualizar clientes")
print("4.- Eliminar clientes")

clientes = [] #Creo una lista VACIA

while True: #Esto desata un bucle infinito pero controlado

#Le permito escoger una opcion
    opcion = input("Escoge una opcion: ")
    opcion = int(opcion) #Convierto a entero


    if opcion == 1:
        print("Vamos a insertar un cliente")
    elif opcion == 2:
        print("Vamos a ver los clientes")
    elif opcion == 3:
        print("Vamos a actualizar un cliente")
    elif opcion == 4:
        print("Vamos a eliminar un cliente")
    else:
        break