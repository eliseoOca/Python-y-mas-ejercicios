entrada=int(input('primer numero: '))
salida=int(input('ultimo numero: '))
print('devolver los numero pares alreves \n')
for x in range(salida,entrada-1,-1):
    if x % 2 ==0:
        print(x)