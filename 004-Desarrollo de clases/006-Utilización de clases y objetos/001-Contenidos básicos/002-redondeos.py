class Matematicas():
    def __init__(self):
        self.PI = 3.14159265359
    
    def redondeo(self,numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondea = 0
        else:
            redondea = 1
        return entero + redondea

    def techo(self,numero):
        return int(numero)+1
    def suelo(self,numero):
        return int(numero)

Mate = Matematicas()
print(Mate.redondeo(4.7))
print(Mate.redondeo(4.2))
print(Mate.techo(4.7))
print(Mate.suelo(4.7))