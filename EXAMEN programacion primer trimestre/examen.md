- En el desarrollo de aplicaciones, es esencial contar con una interfaz que permita al usuario interactuar con la base de datos. Esto es muy util, ya que facilita mucho el trabajo de insertar datos en la base de datos. 

- La finalidad es ofrecer una herramienta funcional que facilite la administración de piezas dentro del portafolio, permitiendo al usuario modificar los datos sin necesidad de acceder directamente al gestor de base de datos. Este tipo de aplicación es muy útil en entornos reales donde se requiere una gestión dinámica y segura de la información.




- Primero importamos la libreria:
`import mysql.connector`


- Establecemos la conexion con la base de datos, y despues, creamos un cursor para ejecutar sentencias SQL:
```
conexion = mysql.connector.connect(  
    host="localhost",
    user="dani",
    password="Dani12345&",
    database="portafolioexamen"
)

cursor = conexion.cursor()
```

- Iniciamos un bucle infinito en el que añadimos las opciones disponibles para el usuario:
```
while True:                            
    print("Selecciona una opcion:")
    print("1.-Crear un registro:")
    print("2.-Listar registros:")
    print("3.-Actualizar registro:")
    print("4.-Eliminar registro:")

    opcion = int(input("Elige tu opcion: "))  
```


- Si la opcion es 1, se piden los datos que hay en la tabla de la base de datos, despues se ejecuta el comando SQL para que los datos se añadan a la base de datos:
```
if opcion == 1:
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        id_categoria = input("Introduce la categoria: ")
        cursor.execute('''
            INSERT INTO piezasportafolio VALUES (
            NULL,
            "'''+titulo+'''",
            "'''+descripcion+'''",
            "'''+fecha+'''",
            '''+id_categoria+'''
            );
            ''')
        conexion.commit()

```

- Si la opcion es 2, se cogen los datos de la tabla piezasportafolios y se muestran uno por uno:
```
elif opcion == 2:
        cursor.execute('''
      SELECT * FROM piezasportafolio;
    ''')
        filas = cursor.fetchall()

        for fila in filas:
            print(fila)
```

- Si la opcion es 3, se piden los datos a actualizar, una vez puestos, el comando SQL los actualiza en la base de datos:
```
elif opcion == 3:
        identificador = input("Introduce el id a actualizar: ")
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        id_categoria = input("Introduce la categoria: ")
        cursor.execute('''
            UPDATE piezasportafolio SET 
            titulo = "'''+titulo+'''",
            descripcion = "'''+descripcion+'''",
            fecha = "'''+fecha+'''",
            id_categoria = '''+id_categoria+'''
            WHERE id = '''+identificador+''';
            ''')
        conexion.commit()
```


- Si la opcion es 4, se le pregunta al usuario cual quiere eliminar, y el comando SQL elimina de la base de datos el ID elegido:
```
elif opcion == 4:
        id = input("Introduce el id a eliminar: ")
        cursor.execute('''
            DELETE FROM piezasportafolio
            WHERE id = '''+id+'''
            ''')
        conexion.commit()
```



- A contuniacion se muestra un ejercicio en Python que se conecta con una base de datos gracias a mysql.connector, en este Python se le permite al usuario crear, listar, actualizar y eliminar un registro en la base de datos:
```
# Programa registros
# v0.1 Daniel Calve Pardo 2025
# Este programa permite crear, listar, actualizar y eliminar datos de una base de datos.





import mysql.connector    # Importamos la libreria

print("Bienvenidos a la aplicacion")


# Nos conectamos a la base de datos
conexion = mysql.connector.connect(  
    host="localhost",
    user="dani",
    password="Dani12345&",
    database="portafolioexamen"
)

cursor = conexion.cursor()

while True:                             # Creamos el bucle
    print("Selecciona una opcion:")
    print("1.-Crear un registro:")
    print("2.-Listar registros:")
    print("3.-Actualizar registro:")
    print("4.-Eliminar registro:")

    opcion = int(input("Elige tu opcion: "))  # Pedimos que elijan la opcion

    if opcion == 1:
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        id_categoria = input("Introduce la categoria: ")
        cursor.execute('''
            INSERT INTO piezasportafolio VALUES (
            NULL,
            "'''+titulo+'''",
            "'''+descripcion+'''",
            "'''+fecha+'''",
            '''+id_categoria+'''
            );
            ''')
        conexion.commit()
    
    elif opcion == 2:
        cursor.execute('''
      SELECT * FROM piezasportafolio;
    ''')
        filas = cursor.fetchall()

        for fila in filas:
            print(fila)
    
    elif opcion == 3:
        identificador = input("Introduce el id a actualizar: ")
        titulo = input("Introduce el titulo: ")
        descripcion = input("Introduce la descripcion: ")
        fecha = input("Introduce la fecha: ")
        id_categoria = input("Introduce la categoria: ")
        cursor.execute('''
            UPDATE piezasportafolio SET 
            titulo = "'''+titulo+'''",
            descripcion = "'''+descripcion+'''",
            fecha = "'''+fecha+'''",
            id_categoria = '''+id_categoria+'''
            WHERE id = '''+identificador+''';
            ''')
        conexion.commit()
    
    elif opcion == 4:
        id = input("Introduce el id a eliminar: ")
        cursor.execute('''
            DELETE FROM piezasportafolio
            WHERE id = '''+id+'''
            ''')
        conexion.commit()
```






- Este ejercicio me ha permitido aprender a conectar un archivo Python con una base de datos, a utilizar operaciones CRUD, estructuras de control `while`, el uso de `cursor`...
- Este ejercicio es muy util en un entorno de trabajo, ya que permite facilitar mucho el trabajo de guardar datos en una base de datos. Me ha gustado la facilidad que tiene, ya que no es muy complicado de aprender.



