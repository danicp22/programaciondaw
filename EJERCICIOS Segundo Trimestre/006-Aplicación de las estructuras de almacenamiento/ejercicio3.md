- Una agenda puede representarse en Python con una lista multidimensional, donde cada contacto es otra lista con sus campos (nombre, apellidos, email, teléfono). Para conservar los datos entre ejecuciones, uso persistencia en binario con `pickle`, que permite serializar y deserializar estructuras de Python de forma sencilla. En este ejercicio creo una agenda en memoria, la guardo en un archivo binario y después la recupero para verificar que todo funciona.




- Creamos la matriz multidimensional (lista de listas)

```
agenda = []
```

- Añadimos datos

```
agenda.append(["Daniel", "Calve Pardo", "dani@gmail.com", "600123456"])
agenda.append(["Maria", "Perez Ruiz", "maria@gmail.com", "611222333"])
agenda.append(["Carlos", "Sanchez Diaz", "carlos@gmail.com", "622333444"])
```

- Guardamos la agenda en un archivo binario usando pickle

```
archivo = open("agenda.bin", "wb")
pickle.dump(agenda, archivo)
archivo.close()
```

- Imprimimos un mensaje de confirmación

```
print("Agenda guardada correctamente")
```

- Abrimos el archivo para recuperar la información guardada

```
archivo = open("agenda.bin", "rb")
agenda_recuperada = pickle.load(archivo)
archivo.close()
```

- Mostramos todos los contactos recuperados

```
for contacto in agenda_recuperada:
    print(contacto)
```



- A continuación muestro un ejercicio que, gracias a listas multidimensionales y pickle, guarda y recupera una agenda, usando with open(...) para mayor seguridad y un formato de impresión más legible:
```
# Programa agenda
# Daniel Calve Pardo v0.1 2026
# Este programa se almacenan distintos elementos dentro de una lista

import pickle


agenda = []


agenda.append(["Daniel", "Calve Pardo", "dani@gmail.com", "600123456"])
agenda.append(["Maria", "Perez Ruiz", "maria@gmail.com", "611222333"])
agenda.append(["Carlos", "Sanchez Diaz", "carlos@gmail.com", "622333444"])


archivo = open("agenda.bin", "wb")
pickle.dump(agenda, archivo)
archivo.close()


print("Agenda guardada correctamente")


archivo = open("agenda.bin", "rb")
agenda_recuperada = pickle.load(archivo)
archivo.close()

print("Agenda recuperada:")
for contacto in agenda_recuperada:
    print(contacto)
```


- En este ejercicio he guardado una agenda de contactos como una lista de listas y he comprobado que podía recuperarla correctamente con pickle. Me ha servido para entender cómo serializar datos en binario y cómo estructurar la información de forma clara. A partir de aquí, quiero añadir edición y borrado de contactos, validaciones del email y quizás cambiar a diccionarios para que los campos sean más explícitos.
