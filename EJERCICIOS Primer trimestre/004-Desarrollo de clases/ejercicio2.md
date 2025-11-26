- En la gestión de clientes dentro de una aplicación, es habitual tener que realizar operaciones como insertar nuevos registros, listar los existentes, actualizarlos o eliminarlos. Para ello, se suele utilizar una estructura de menú que permita al usuario interactuar con el sistema de forma sencilla. Este tipo de programas son muy útiles en entornos administrativos, comerciales o educativos, donde se requiere mantener organizada la información de personas o entidades. En este ejercicio, se presenta un sistema básico de gestión de clientes utilizando programación orientada a objetos y estructuras de control como bucles y condicionales.



- Definición de la clase `Cliente`

```
class Cliente():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None
```

Creamos una clase `Cliente` con tres atributos: `email`, `nombre` y `direccion`. Estos atributos se inicializan como `None` en el constructor.

- Menú de opciones

```
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")
```

Se muestra un menú con cuatro opciones para que el usuario pueda interactuar con el sistema.

- Lista de clientes

```
clientes = []
```

Creamos una lista vacía llamada `clientes` donde se almacenarán los objetos de tipo `Cliente`.

- Bucle principal

```
while True:
  opcion = int(input("Escoge una opción: "))
```

Se inicia un bucle infinito controlado por el usuario, que permite repetir el menú hasta que se introduzca una opción no válida (lo que provoca la salida del bucle).

- Opción 1: Insertar cliente

```
if opcion == 1:
  print("Vamos a insertar un cliente")
  nuevocliente = Cliente()
  nuevocliente.nombre = input("Introduce el nombre del cliente: ")
  nuevocliente.email = input("Introduce el email del cliente: ")
  nuevocliente.direccion = input("Introduce la direccion del cliente: ")
  clientes.append(nuevocliente)
```

Se crea un nuevo objeto `Cliente`, se le asignan valores mediante `input`, y se añade a la lista de clientes.

- Opción 2: Listar clientes

```
elif opcion == 2:
  if not clientes:
    print("No hay clientes para ver")
  else:
    for cliente in clientes:
      print(cliente.nombre, cliente.email, cliente.direccion)
```

Se comprueba si la lista está vacía. Si no lo está, se recorren los clientes y se muestran sus datos.

- Opción 3 y 4: Actualizar y eliminar (pendientes de implementación)

```
elif opcion == 3:
  print("Vamos a actualizar un cliente")
elif opcion == 4:
  print("Vamos a eliminar un cliente")
```

Se muestran mensajes indicando que estas funcionalidades están previstas, pero aún no se han desarrollado.

- Salida del programa

```
else:
  break
```

Si el usuario introduce una opción no válida (por ejemplo, 5 o cualquier otro número), el programa termina.





- A continuación se muestra un ejercicio que, mediante clases, listas y condicionales, permite gestionar información de clientes en un sistema interactivo:

```
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
  opcion = int(input("Escoge una opción: "))
  
  if opcion == 1:
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Introduce el nombre del cliente: ")
    nuevocliente.email = input("Introduce el email del cliente: ")
    nuevocliente.direccion = input("Introduce la direccion del cliente: ")
    clientes.append(nuevocliente)
  elif opcion == 2:
    if not clientes:
      print("No hay clientes para ver")
    else:
      for cliente in clientes:
        print(cliente.nombre, cliente.email, cliente.direccion)
  elif opcion == 3:
    print("Vamos a actualizar un cliente")
  elif opcion == 4:
    print("Vamos a eliminar un cliente")
  else:
    break
```





- Este ejercicio me ha ayudado a entender cómo se puede construir un sistema básico de gestión de clientes utilizando clases, listas y estructuras de control. Me parece muy útil para organizar información de forma estructurada y permitir que el usuario interactúe con el programa mediante un menú. En el futuro, me gustaría completar las opciones de actualizar y eliminar para que el sistema esté totalmente funcional.


