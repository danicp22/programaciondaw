import pickle

menu = []

while True:
    print("Opciones:")
    print("1.-Introducir nueva comida en el menu")
    print("2.-Listar comidas en el menu")
    print("3.-Guardar en archivo")
    print("4.-Cargar datos de archivo")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        comida = input("Introduce el nombre de la comida: ")
        menu.append(comida)
    elif opcion == 2:
        print("Tu comida hasta el momento es: ")
        for elemento in menu:
            print(elemento)
    elif opcion == 3:
        archivo = open("datos.bin","wb")   # Write Binary
        pickle.dump(menu,archivo)
        archivo.close()
        print("Se ha guardado con exito ✅")
    elif opcion == 4:
        archivo = open("datos.bin","rb")
        menu = pickle.load(archivo)  # Volcamos el archivo a la lista
        archivo.close()