import random as xdlol

patron = {1,2,3,4,5,6,7,8,9}

while True:
  lista = []

  for i in range(1,10):
    lista.append(xdlol.randint(1,9))
  conjunto = set(lista)

  if conjunto == patron:
    print("El conjunto es correcto")
    print(conjunto)
    print(lista)
    #Ahora elimino un numero
    indice = xdlol.randint(1,9)
    lista[indice] = "_"
    print(lista)
    break
