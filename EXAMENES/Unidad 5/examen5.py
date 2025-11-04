import pickle

# Creamos la clase y as
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

clientes = []

# Usamos pickle
try:  
  archivo = open("clientes.bin",'rb')
  clientes = pickle.load(archivo)
  archivo.close()
except:
  print("No existe archivo de datos")

while True:
    archivo = open("clientes.bin",'wb')
    pickle.dump(clientes,archivo)
    archivo.close()
    
    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Salir")
    opcion = int(input("Escoge una opcion: "))
    
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        email = input("Introduce el email: ")
        clientes.append(Cliente(nombre,apellidos,email))
        print("Cliente guardado correctamente")
    elif opcion == 2:
        for cliente in clientes:
            print(cliente.nombre,cliente.apellidos,cliente.email)
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Intente de nuevo")
        
