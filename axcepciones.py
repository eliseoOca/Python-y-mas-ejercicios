import os

num1=45
num2=0
try:
    resultado=num1/num2
except:
    resultado=0
    print('ha ocurrido un error')
finally:
    print(resultado)
    print('esto se ejecuta siempre')
try:
    os.remove(os.getcwd()+'/archivo454.txt')
except FileNotFoundError:
    print('el archivo no se encuentra en el directorio, no puedo borrarlo')
finally:
    print('fin de la ejecucion del script')

