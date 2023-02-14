#calculadora vasica

def menu():
    print('1. sumar')
    print('2. restar')
    print('3. multiplicar')
    print('4. dividir')
    print('0. salir')
    opcion = int(input('?__'))
    return opcion

def solicitaDatos():
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    if num2==0:
        print('el numero no puede ser 0 \n')
        num2= int(input("Ingrese el segundo numero: "))
    return num1,num2

def operacion(operador,num1,num2):
    if operador == 'suma':
        resultado=num1+num2
    elif operador == 'resta':
        resultado=num1-num2
    elif operador == 'multiplica':
        resultado=num1*num2
    elif operador=='divide':
        resultado=num1/num2
    return resultado   
        
while True:
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} + {num2}es = ")
        print(operacion('suma', num1, num2))
    elif opcion == 2:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} - {num2}es = ")
        print(operacion('resta', num1, num2))
    if opcion == 3:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} * {num2}es = ")
        print(operacion('multiplica', num1, num2))
    if opcion == 4:
        num1, num2 = solicitaDatos()
        print(f"El resultado de {num1} / {num2}es = ")
        print(operacion('divide', num1, num2))
    if opcion == 0:
        break
    else:
        print('Introduce una opcion valida')
        