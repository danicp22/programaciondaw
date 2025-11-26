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
