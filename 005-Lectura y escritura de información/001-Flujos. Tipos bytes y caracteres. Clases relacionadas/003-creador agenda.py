while True:
    print("Dime lo que quieres hacer: ")
    print("1.-Introduce un nuevo contacto")
    print("2.-Leer todos los contacos")
    opcion = input("Escoge tu opcion: ")
    opcion = int(opcion)
    if opcion == 1:
        nombre = input("Introduce el nombre de la persona ")
        email = input("Introduce el email de la persona ")
        archivo = open("agenda.txt",'w')
        archivo.write(nombre+","+email+"\n")
        archivo.close()
    elif opcion == 2:
        archivo = open("agenda.txt",'r')
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
        archivo.close()