entrada = int(input('ingrese el numero de entrada: '))
salida = int(input('Ingrese el numero de salida: '))
print('ver secuensia de numero impares \n')
for x in range(entrada,salida+1):
    if x%2!=0:
        print(x)
    