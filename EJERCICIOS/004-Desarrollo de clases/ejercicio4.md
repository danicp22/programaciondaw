- En el desarrollo de aplicaciones orientadas a objetos, es fundamental proteger los datos internos de las clases para evitar accesos no deseados o modificaciones incorrectas. Para ello, se utilizan atributos privados junto con métodos públicos que permiten establecer (`set`) y obtener (`get`) los valores de dichos atributos. Este enfoque garantiza un mayor control sobre la información y facilita la validación de datos. En este ejercicio, trabajaremos con una clase llamada `Cliente`, que representa a una persona con nombre completo y correo electrónico, y aprenderemos a manipular sus datos de forma segura mediante métodos `get` y `set`.




- Definición de la clase `Cliente`

```
class Cliente:
```

Creamos una clase llamada `Cliente` que encapsulará los datos de un cliente.

- Constructor con atributos privados

```
def __init__(self):
    self.__nombrecompleto = ""
    self.__email = ""
```

El constructor `__init__` inicializa dos atributos privados: `__nombrecompleto` y `__email`. El uso de doble guión bajo (`__`) indica que estos atributos no deben ser accedidos directamente desde fuera de la clase.

- Métodos `set` (establecer valores)

```
def setNombreCompleto(self, nuevonombre):
    self.__nombrecompleto = nuevonombre
```

Este método permite asignar un nuevo valor al atributo `__nombrecompleto`.

```
def setEmail(self, nuevoemail):
    self.__email = nuevoemail
```

Este método permite asignar un nuevo valor al atributo `__email`.

- Métodos `get` (obtener valores)

```
def getNombreCompleto(self):
    return self.__nombrecompleto
```

Este método devuelve el valor actual del atributo `__nombrecompleto`.

```
def getEmail(self):
    return self.__email
```

Este método devuelve el valor actual del atributo `__email`.





- A continuación se muestra un ejercicio que, gracias a métodos `get` y `set`, permite establecer y mostrar los datos de un cliente como su nombre completo y su correo electrónico:

```
# Programa metodos
# v0.1 Daniel Calve Pardo 2025
# Este programa utiliza metodos get y set para establecer valores 

# Definir la Clase Cliente
class Cliente:
    # Constructor con atributos privados
    def __init__(self):
        self.__nombrecompleto = ""
        self.__email = ""

    # Métodos Setters
    def setNombreCompleto(self, nuevonombre):
        self.__nombrecompleto = nuevonombre

    def setEmail(self, nuevoemail):
        self.__email = nuevoemail

    # Métodos Getters
    def getNombreCompleto(self):
        return self.__nombrecompleto

    def getEmail(self):
        return self.__email

# Instanciar y Utilizar la Clase Cliente
cliente1 = Cliente()

# Establecer valores con setters
cliente1.setNombreCompleto("Daniel Calve")
cliente1.setEmail("dani@example.com")

# Mostrar valores con getters
print("Nombre completo:", cliente1.getNombreCompleto())
print("Email:", cliente1.getEmail())
```





- Este ejercicio me ha servido para entender cómo se utilizan los métodos `get` y `set` en una clase para trabajar con atributos privados. Me parece muy útil este enfoque porque permite mantener la integridad de los datos y controlar cómo se accede a ellos. Además, me ha ayudado a reforzar el concepto de encapsulamiento en programación orientada a objetos.


