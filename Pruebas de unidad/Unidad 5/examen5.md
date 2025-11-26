- Este ejercicio consiste en crear una mini-aplicación CRUD para gestionar clientes. El usuario puede insertar nuevos clientes o listar los existentes. Para mantener los datos entre ejecuciones, se utiliza la librería `pickle`, que permite guardar la lista de clientes en un archivo binario. En esta versión, el guardado se realiza en cada ciclo del bucle, lo que garantiza que los datos estén siempre actualizados, incluso si se interrumpe el programa inesperadamente.




1.  Importación de librerías
    ```
    import pickle
    ```
    Se importa la librería `pickle`, que permite guardar y recuperar objetos de Python en archivos binarios.

2.  Definición de la clase `Cliente`
    ```p
    class Cliente():
        def __init__(self, nombre, apellidos, email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
    ```
    Se define una clase llamada `Cliente` con tres propiedades: `nombre`, `apellidos` y `email`. No tiene métodos adicionales.

3.  Inicialización de la lista de clientes
    ```
    clientes = []
    ```
    Se crea una lista vacía que almacenará los objetos `Cliente`.

4.  Lectura del archivo binario con `pickle`
    ```
    try:  
        archivo = open("clientes.bin", 'rb')
        clientes = pickle.load(archivo)
        archivo.close()
    except:
        print("No existe archivo de datos")
    ```
    Se intenta abrir el archivo `clientes.bin` en modo lectura binaria (`'rb'`).
    *   Si el archivo existe, se carga su contenido (una lista de clientes) con `pickle.load`.
    *   Si no existe o hay error, se muestra un mensaje y se continúa con la lista vacía.

5.  Inicio del bucle `while True`
    ```
    while True:
    ```
    Se inicia un bucle infinito que mostrará el menú y permitirá al usuario interactuar.

6.  Guardado automático de clientes al inicio de cada iteración
    ```
        archivo = open("clientes.bin", 'wb')
        pickle.dump(clientes, archivo)
        archivo.close()
    ```
    Se abre el archivo en modo escritura binaria (`'wb'`) y se guarda la lista actualizada de clientes con `pickle.dump`.

7.  Menú de opciones
    ```
        print("Escoge una opción:")
        print("1.-Insertar un cliente")
        print("2.-Listar clientes")
        print("3.-Salir")
        opcion = int(input("Escoge una opcion: "))
    ```
    Se muestra el menú al usuario y se recoge su elección como número entero.

8.  Opción 1: Insertar cliente
    ```
        if opcion == 1:
            nombre = input("Introduce el nombre: ")
            apellidos = input("Introduce los apellidos: ")
            email = input("Introduce el email: ")
            clientes.append(Cliente(nombre, apellidos, email))
            print("Cliente guardado correctamente")
    ```
    Si el usuario elige la opción 1:
    *   Se piden los datos del cliente.
    *   Se crea un objeto `Cliente` con esos datos.
    *   Se añade a la lista `clientes`.
    *   Se muestra un mensaje de confirmación.

9.  Opción 2: Listar clientes
    ```
        elif opcion == 2:
            for cliente in clientes:
                print(cliente.nombre, cliente.apellidos, cliente.email)
    ```
    Si el usuario elige la opción 2:
    *   Se recorre la lista de clientes.
    *   Se imprime el nombre, apellidos y email de cada uno.

10. Opción 3: Salir del programa

```
    elif opcion == 3:
        print("Saliendo del programa...")
        break
```

Si el usuario elige la opción 3:

*   Se muestra un mensaje de salida.
*   Se rompe el bucle con `break`.

11. Opción no válida

```
    else:
        print("Opcion no valida. Intente de nuevo")
```

Si el usuario introduce un número que no corresponde a ninguna opción:

*   Se muestra un mensaje de error.





- A continuación se muestra un ejercicio que, gracias a entradas del usuario, estructuras condicionales y persistencia con pickle, permite crear una lista de clientes, guardarla en un archivo binario y recuperarla automáticamente al iniciar el programa. El menú interactivo permite insertar nuevos clientes o listar los existentes.

```
import pickle

# Creamos la clase Cliente con propiedades
class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

clientes = []

# Intentamos cargar los clientes desde archivo
try:  
    archivo = open("clientes.bin", 'rb')
    clientes = pickle.load(archivo)
    archivo.close()
except:
    print("No existe archivo de datos")

# Bucle principal
while True:
    # Guardamos los clientes al inicio de cada iteración
    archivo = open("clientes.bin", 'wb')
    pickle.dump(clientes, archivo)
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
        clientes.append(Cliente(nombre, apellidos, email))
        print("Cliente guardado correctamente")
        
    elif opcion == 2:
        for cliente in clientes:
            print(cliente.nombre, cliente.apellidos, cliente.email)
            
    elif opcion == 3:
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida. Intente de nuevo")
```



- Este ejercicio ha sido una excelente práctica para construir una aplicación funcional que permite gestionar clientes de forma sencilla. Gracias al uso de un menú interactivo, el usuario puede insertar nuevos registros o consultar los existentes, todo ello con una experiencia fluida y clara.
La incorporación de la librería pickle ha permitido que los datos se conserven entre ejecuciones, lo que convierte esta aplicación en una herramienta útil y persistente. Además, el guardado automático en cada ciclo del programa aporta seguridad ante posibles cierres inesperados.
Este tipo de ejercicios no solo ayudan a afianzar la lógica de programación, sino que también preparan el terreno para desarrollar aplicaciones más completas y profesionales. A partir de aquí, se pueden añadir nuevas funcionalidades como modificar o eliminar clientes, validar datos o exportar la información a otros formatos.