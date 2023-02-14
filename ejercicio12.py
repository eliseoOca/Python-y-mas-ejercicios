class Vehiculo():
    def __init__(self, marca,color):
        self.marca=marca
        self.color=color
    def __str__(self):
        return 'El vehiculo de marca {}, es de color {}'.format(self.marca,self.color)
class auto(Vehiculo):
    def __init__(self,marca,color,portencia,motor):
        Vehiculo.__init__(self,marca,color)
        self.portencia=portencia
        self.motor=motor
    def __str__(self):
        return Vehiculo.__str__(self) + '. {} '.format(self.portencia, self.motor)
    
mi_auto=Vehiculo('Fiat','Negro')
print(mi_auto)
mi_motor=auto('Fiar','Negro','1200','nafta')
print(mi_motor)
        
        