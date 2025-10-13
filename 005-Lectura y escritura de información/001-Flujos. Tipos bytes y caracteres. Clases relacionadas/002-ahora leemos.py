archivo = open("clientes.txt",'r') #R = read

contenido = archivo.readline()
#Tambien existe archivo.readlines()

print(contenido)

archivo.close()