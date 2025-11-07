# Programa gestion de informacion
# v0.1 Daniel Calve Pardo 2025
# Este programa gestiona informacion sobre clientes

class Cliente():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None


# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

clientes = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado

  # Le permito escoger una opción
  opcion = int(input("Escoge una opción: "))

  
  if opcion == 1:
    print("Vamos a insertar un cliente")
    # Primero creamos un nuevo cliente
    nuevocliente = Cliente()
    # Ahora le ponemos propiedades
    nuevocliente.nombre = input("Introduce el nombre del cliente: ")
    nuevocliente.email = input("Introduce el email del cliente: ")
    nuevocliente.direccion = input("Introduce la direccion del cliente: ")
    # A la lista de clientes añadimos nuestro cliente
    clientes.append(nuevocliente)
  elif opcion == 2:
        if not clientes:
            print("No hay clientes para ver")
        else:
            for cliente in clientes:
                print(cliente.nombre,cliente.email,cliente.direccion)
  elif opcion == 3:
    print("Vamos a actualizar un cliente")
  elif opcion == 4:
    print("Vamos a eliminar un cliente")
  else:
    break
    
    
    
    
    
    
    
    
    
    
    