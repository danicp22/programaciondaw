- En programación orientada a objetos, una clase representa un modelo que agrupa datos (propiedades) y comportamientos (métodos). En este ejercicio, vamos a crear una clase llamada Cliente, que representa a una persona con datos como nombre, apellidos y correo electrónico. Además, implementaremos métodos para modificar y acceder a sus propiedades, y crearemos varias instancias para demostrar su funcionamiento.


- Primero definimos la clase cliente: `class Cliente():`

- Se define un constructor (en este caso `__init__`) y se crean propiedades para la clase:
```
def __init__(self,nombre,apellidos,email,telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
```

- Creamos los metodos get y set, el metodo set permite modificar, en este caso, el correo del cliente. El metodo get permite acceder al correo del cliente:
```
# Metodo set     
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
        
    # Metodo get
    def getEmail(self):
        return self.email
```

- Se crean tres instancias de la clase:
```
cliente1 = Cliente("Daniel", "Calve Pardo", "dani@gmail.com", "657483932")
cliente2 = Cliente("Jorge", "Gomez Perez", "jorge@gmail.com", "678590499")
cliente3 = Cliente("Antonio", "Recio Matamoros", "mariscosrecio@gmail.com", "647567465")
```

- Primero imprimimos los datos originales:
```
print("Datos originales")
print(cliente1.getEmail())
print(cliente2.getEmail())
print(cliente3.getEmail())
```

- A continuacion usamos el metodo set para cambiar estos datos:
```
cliente1.setEmail("cliente1@gmail.com")
cliente2.setEmail("cliente2@gmail.com")
cliente3.setEmail("cliente3@gmail.com")
```

- Y por ultimo mostramos los nuevos datos:
```
print("Nuevos datos")
print(cliente1.getEmail())
print(cliente2.getEmail())
print(cliente3.getEmail())
```



- A continuación se muestra un ejercicio que, gracias a clases, constructores y métodos, permite crear clientes y modificar sus datos:
```
# Programa Desarrollo de clases
# v0.1 Daniel Calve Pardo 2025
# En este programa se crea una clase, se le añaden propiedades, metodos, constructores, instancias y se demuestra que todo funcione.


class Cliente():
    # Constructor con parametros
    def __init__(self,nombre,apellidos,email,telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        
        
    # Metodo set     
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
        
    # Metodo get
    def getEmail(self):
        return self.email
    
     
     
# Creamos tres instancias de la clase Cliente
cliente1 = Cliente("Daniel", "Calve Pardo", "dani@gmail.com", "657483932")
cliente2 = Cliente("Jorge", "Gomez Perez", "jorge@gmail.com", "678590499")
cliente3 = Cliente("Antonio", "Recio Matamoros", "mariscosrecio@gmail.com", "647567465")

# Mostramos los datos originales
print("Datos originales")
print(cliente1.getEmail())
print(cliente2.getEmail())
print(cliente3.getEmail())


# Modificamos los datos originales
cliente1.setEmail("cliente1@gmail.com")
cliente2.setEmail("cliente2@gmail.com")
cliente3.setEmail("cliente3@gmail.com")


# Mostramos los nuevos datos
print("Nuevos datos")
print(cliente1.getEmail())
print(cliente2.getEmail())
print(cliente3.getEmail())
```


- Este ejercicio muestra cómo crear una clase en Python con propiedades y métodos personalizados. El uso de set y get permite modificar y acceder a los datos de forma controlada. Además, al instanciar varios objetos, se demuestra cómo cada cliente puede tener sus propios datos y comportamientos. Este tipo de estructura es muy útil en aplicaciones que gestionan usuarios, clientes o cualquier entidad con atributos.