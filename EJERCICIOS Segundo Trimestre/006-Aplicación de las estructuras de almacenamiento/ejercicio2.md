- Las aplicaciones de consola con menús son ideales para practicar estructuras de control, listas y persistencia de datos. Este programa gestiona un “menú de comidas”: permite añadir elementos, listarlos y guardarlos en un archivo binario (`datos.bin`) usando `pickle`. 



- Importamos el módulo `pickle` para serializar la lista (convertir a bytes) y guardarla en un archivo.

`import pickle`


- Creamos una lista vacia
`menu = []`



Creamos un bucle infinito con un menú y lectura de la opción por teclado como cadena.
```
while True:
    print("MENÚ DE COMIDAS")
    ...
    opcion = input("Selecciona una opción: ")
```



- Añadimos la opcion de añadir

```
if opcion == "1":
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
    print("Comida añadida correctamente.")
```


- Añadimos la opcion de listar

```
elif opcion == "2":
    if len(menu) == 0:
        print("El menú está vacío.")
    else:
        print("Comidas en el menú:")
        for comida in menu:
            print("-", comida)
```



- Añadimos la opcion de guardar

```
elif opcion == "3":
    with open("datos.bin", "wb") as archivo:
        pickle.dump(menu, archivo)
    print("Menú guardado correctamente en 'datos.bin'.")
```


- Añadimos la opcion de salir
```
elif opcion == "4":
    print("Saliendo del programa...")
    break
```



- A continuación muestro un ejercicio que, gracias a listas, validaciones y persistencia con `pickle`, gestiona un menú de comidas con carga, guardado y borrado por índice.

```
# Programa meu de comidas
# Daniel Calve Pardo v0.1 2026
# Este programa añade, lista y guarda comidas

import pickle

# 1. Crear una lista vacía
menu = []

while True:
    print("MENÚ DE COMIDAS")
    print("1. Introducir nueva comida en el menú")
    print("2. Listar comidas en el menú")
    print("3. Guardar en archivo")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    # Opción 1: Añadir comida
    if opcion == "1":
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)
        print("Comida añadida correctamente.")

    # Opción 2: Listar comidas
    elif opcion == "2":
        if len(menu) == 0:
            print("El menú está vacío.")
        else:
            print("Comidas en el menú:")
            for comida in menu:
                print("-", comida)

    # Opción 3: Guardar en archivo
    elif opcion == "3":
        with open("datos.bin", "wb") as archivo:
            pickle.dump(menu, archivo)
        print("Menú guardado correctamente en 'datos.bin'.")

    # Opción 4: Salir
    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

```


- En este ejercicio he trabajado con un menú interactivo que me permite añadir comidas, listarlas, borrarlas y guardarlas en un archivo binario. Con este programa he entendido mejor cómo usar listas, cómo manejar entradas del usuario y cómo guardar datos con pickle para que no se pierdan cuando cierro la aplicación.