#primera for de importar paquetes
#import paquetes.funcion

#sefunda forma de importar paquetes
#from paquetes.funcion import suma as suma

#aca se hace con la tercera forma
from paquetes.funcion import *

#aca se hace con la primera forma
#print(paquetes.funcion.esPar(25))
#print(paquetes.funcion.esPar(64))

#aca se hace con la segunda forma
print(suma(23,45))

#aca se hace con la tercera forma 
print(esPar(64))
print(esPar(25))

