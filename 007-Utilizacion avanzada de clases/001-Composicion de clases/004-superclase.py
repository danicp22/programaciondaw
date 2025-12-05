class Persona():
  def __init__(self,nombre,apellidos,email): 
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
  def dameDatos(self):
    return self.nombre+self.apellidos  


class Profesor(Persona):
  def __init__(self,nombre,apellidos,email):
  	super().__init__(nombre, apellidos, email)


class Alumno(Persona):
  def __init__(self,nombre,apellidos,email):
  	super().__init__(nombre, apellidos, email)
    
alumno1 = Alumno("Daniel","Calve","daniel@example.com")
print(alumno1.dameDatos())

profesor1 = Profesor("Jose Vicente","Carratala","info@jocarsa.com")
print(profesor1.dameDatos())