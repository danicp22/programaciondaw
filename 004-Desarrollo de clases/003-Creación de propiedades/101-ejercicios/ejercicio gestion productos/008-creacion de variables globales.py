'''
Aplicacion de gestion de productos
(c) 2025 Daniel Calve Pardo
Esta aplicacion gestiona productos
'''

#En esta aplicion no aplica importar librerias

#Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

#Creamos las variables globales

productos = []

#Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Daniel Calve Pardo")
#Le mostramos al usuario las opciones que tiene
print("Selecciona una opcion:")
print("1.-Crear un nuevo producto")
print("2.-Listar productos")
print("3.-Actualizar productos")
print("4.-Eliminar productos")
opcion = int(input("Escoge tu opcion: "))
#En funcion de la opcion que coja el usuario
if opcion == 1:
    #O bien creamos un nuevo producto
    print("Creamos un nuevo producto")
elif opcion ==2:
    #O bien listamos los productos
    print("Vamos a listar productos")
elif opcion == 3:
    #O bien actualizamos los productos
    print("Vamos a actualizar productos")
elif opcion == 4:
    #O bien eliminamos los productos
    print("Vamos a eliminar productos")
#Y volvemos a repetir 