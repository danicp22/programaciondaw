
class Profesor():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    

class Alumno():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
alumno1 = Alumno("Daniel","Calve","dani@example.com")
print(alumno1)

profesor1 = Profesor("Jose","Carratala","hola@example.com")
print(profesor1)
