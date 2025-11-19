class Cliente():
  def __init__(self,nuevonombre,nuevoemail):
    self.nombre = nuevonombre
    self.email = nuevoemail

clientes = []

clientes.append(Cliente("Daniel","dani@dani.com"))
clientes.append(Cliente("Juan","juan@jocarsa.com"))

print(clientes)
