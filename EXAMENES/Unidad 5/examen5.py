import pickle

class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

print("### Gestión de clientes v0.1 ###")
print("### Daniel Calve Pardo ###")

clientes = []

try:
    archivo = open("clientes.bim", "rb")
    clientes = pickle.load(archivo)
    archivo.close()
    print("Datos cargados correctamente.")
except:
    print("No existe el archivo de datos, se creará uno nuevo.")


while True:
    print("\nEscoge una opción: ")
    print("1.- Insertar un cliente")
    print("2.- Listar clientes")
    print("3.- Salir del menú")

    opcion = int(input("Escoge una opción: "))

    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")

        clientes.append(Cliente(nombre, apellidos, email))
        print("Cliente añadido correctamente.")

    elif opcion == 2:
        # Mostramos todos los clientes
        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:
            identificador = 0
            for cliente in clientes:
                print("Cliente ID:", identificador)
                print("Nombre:", cliente.nombre)
                print("Apellidos:", cliente.apellidos)
                print("Email:", cliente.email)
                identificador += 1

    elif opcion == 3:
        # Guardamos la lista de clientes antes de salir
        archivo = open("clientes.bin", "wb")
        pickle.dump(clientes, archivo)        # Guardamos la lista completa
        archivo.close()
        print("Datos guardados correctamente. Adios :)")
        break

    else:
        print("Opción no válida, intenta de nuevo.")