numero1=int(input("ingrese primer numero: "))
numero2=int(input("ingrese segundo numero: "))

if (numero1>numero2):
    print(f"0el numero{numero1} es mayor que el primero {numero2}")
elif (numero1<numero2):
    print(f"El numero {numero1} es menor que el numero {numero2}")
else:
    print("Los dos numeros son iguales")
    
print("Programa finalizado")    

#segundo ejemplo, edades por tarifa

edad= int(input("Ingrese la edad y para indicar la tarifa: "))
if edad<5:
    precio=0
elif edad<15:
    precio=5
elif edad<65:
    precio=20
else:
    precio=15
print("Tu tarifa para entrar es de "+str(precio))