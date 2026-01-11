- En programación, las listas de Python nos permiten almacenar colecciones de elementos ordenados y modificables, como nombres de eventos o peleas. En este ejercicio trabajo con una lista de eventos de MMA para añadir, consultar, modificar y eliminar elementos






- Creamos la lista
```
lista_de_mma_fights = [
    "UFC 200",
    "Bellator 176",
    "Strikeforce 94",
    "Ultimate Fighter 18",
    "MMA Fighting Championship"
]
```

- Añadimos una pelea a la lista
`lista_de_mma_fights.append("UFC 205")`


- Imprimimos la lista
`print(lista_de_mma_fights)`

- Accedemos al segundo elemento de la lista
`print(lista_de_mma_fights[1])`

- Sobreescribimos el tercer elemento de la lista
`lista_de_mma_fights[2] = "Ultimate Fighter 21"`

- Imprimimos la lista actualizada
`print(lista_de_mma_fights)`

- Eliminamos el ultimo elemento
`lista_de_mma_fights.pop()`


- Imprimimos la lista final
`print(lista_de_mma_fights)`



- A continuación muestro un ejercicio que, gracias a operaciones básicas de listas (adición, consulta, modificación y eliminación), gestiona una lista de peleas de MMA:
```
# Programa Listas Python
# Daniel Calve Pardo v0.1 2026
# En este programa vamos a crear una lista  y vamos a añadir peleas


lista_de_mma_fights = [
    "UFC 200",
    "Bellator 176",
    "Strikeforce 94",
    "Ultimate Fighter 18",
    "MMA Fighting Championship"
]

lista_de_mma_fights.append("UFC 205")


print(lista_de_mma_fights)

print(lista_de_mma_fights[1])

lista_de_mma_fights[2] = "Ultimate Fighter 21"

print(lista_de_mma_fights)

lista_de_mma_fights.pop()

print(lista_de_mma_fights)
```




- He usado una lista para gestionar eventos de MMA y he aplicado operaciones clave: añadir con append, consultar por índice, modificar por posición y eliminar con pop. 