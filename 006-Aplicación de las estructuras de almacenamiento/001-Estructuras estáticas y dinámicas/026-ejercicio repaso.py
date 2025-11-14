print("Competicion v0.1")
import json  # Para usar la libreria tengo que importarla
archivo = open("competicion.json","w")  # Abro un archivo

competicion = []

while True:
    print("Selecciona una opcion")
    print("1.-Añadir elemento a la lista")
    print("2.-Leer la lista")
    opcion = int(input("Tu opcion: "))
    
    if opcion == 1:
        print("Añadimos una competicion a la lista:")
        lugar = input("Indica el lugar de la competicion: ")
        fecha = input("Indica la fecha de la competicion: ")
        peleas = input("Indica cuantas peleas van a realizarse: ")
        competicion.append({"lugar":lugar,"fecha":fecha,"peleas":peleas})
        archivo = open("competicion.json","w")        # Abro el archivo
        json.dump(competicion,archivo)       # Guardo en json
        archivo.close()                               # Cierro el archivo
        
    elif opcion == 2:
        print("Listamos las comnpeticiones:")
        for velada in competicion:
            print("Lugar:",velada['lugar'])
            print("Fecha:",velada['fecha'])
            print("Peleas:",velada['peleas'])
            print("###############################")   # Esto es estetico, es un separador