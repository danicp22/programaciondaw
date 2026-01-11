# Programa agenda
# Daniel Calve Pardo v0.1 2026
# Este programa se almacenan distintos elementos dentro de una lista

import pickle

# Creamos la matriz multidimensional
agenda = []

# Añadimos datos 
agenda.append(["Daniel", "Calve Pardo", "dani@gmail.com", "600123456"])
agenda.append(["Maria", "Perez Ruiz", "maria@gmail.com", "611222333"])
agenda.append(["Carlos", "Sanchez Diaz", "carlos@gmail.com", "622333444"])

# Guardamos la agenda en un archivo binario usando pickle
archivo = open("agenda.bin", "wb")
pickle.dump(agenda, archivo)
archivo.close()

print("Agenda guardada correctamente")

# Comprobamos que se puede recuperar la información
archivo = open("agenda.bin", "rb")
agenda_recuperada = pickle.load(archivo)
archivo.close()

print("Agenda recuperada:")
for contacto in agenda_recuperada:
    print(contacto)
