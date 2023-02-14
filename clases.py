class Vehiculo:
    def __init__(self, color, valocidadMaxima, marca):
        self.color=color
        self.velocidadMaxima=valocidadMaxima
        self.velocidad=0
        self.marca=marca
        
    def arrancar(self):
        print('arrancado')
        
    def acelerar(self):
        if self.velocidad==0:
            self.velocidad=10
        else:
            self.velocidad=self.velocidad + 10
        print(f'velocidad = {self.velocidad}')
        
    def frenar(self):
        if self.velocidad>10:
            self.velocidad=self.velocidad - 10
        else:
            self.velocidad=0
        print(f'velocidad={self.velocidad}')
        
    def estado(self):
        print(f'soy de la marca {self.marca}, con un color {self.color} y velocidad maxima de {self.velocidadMaxima}')
    
class moto(Vehiculo):
    def __init__(self, color, valocidadMaxima, marca, ruedas=2):
        Vehiculo.__init__(self,color,valocidadMaxima,marca)
        self.ruedas=ruedas
    
    def estado(self):
        print(f'soy de la marca {self.marca}, con un color {self.color} y velocidad maxima de {self.velocidadMaxima} y tengo{self.ruedas} ruedas')
        
class auto(Vehiculo):
    def __init__(self, color, valocidadMaxima, marca, ruedas=4):
        Vehiculo.__init__(self,color,valocidadMaxima,marca)
        self.ruedas=ruedas
    
    def estado(self):
        print(f'soy de la marca {self.marca}, con un color {self.color} y velocidad maxima de {self.velocidadMaxima} y tengo{self.ruedas} ruedas')
        
peugeot = auto('rojo',120,'Peugeot',4)
peugeot.arrancar()
peugeot.acelerar()
peugeot.estado()
peugeot.acelerar()

renault=auto('verde',130,'Renault',4)
renault.arrancar()
renault.acelerar()
renault.acelerar()
renault.estado()

yamaha= moto('azul',140,'yamaha',2)
yamaha.arrancar()
yamaha.acelerar()
yamaha.acelerar()
yamaha.frenar()
yamaha.estado()
        