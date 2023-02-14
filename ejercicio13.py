class Alumno():
    def __init__(self,nombre,notas):
        self.nombre=nombre
        self.notas=notas
    def __str__(self):
        
        return 'El alumno {}, ha sacadp un  {}'.format(self.nombre, self.notas)
        
    def aprobado(self):
        if self.notas<5:
            return False
        else:
            return True
        
eliseo=Alumno('eliseo',8)
print(eliseo)
aprobado=eliseo.aprobado()
if aprobado:
    print('estoy aprobado')
else:
    print('estoy desaprobado')
        