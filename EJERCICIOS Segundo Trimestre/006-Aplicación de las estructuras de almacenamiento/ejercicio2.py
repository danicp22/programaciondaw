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
