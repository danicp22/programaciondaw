#pip3 install pickle | pip install pickle
import pickle

archivo = open("datos.bin","wb")
cadena = "Dani"

pickle.dump(cadena,archivo)

archivo.close()
