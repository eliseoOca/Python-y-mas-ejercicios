#tabla de multiplicar
tabla = int(input("Que tabla quieres calcular? "))
#creamos variable contador
contador=1
print(f"Tabla del {tabla}")
#repeticion
for contador in range(1,11):
    resultado = tabla * contador
    print(f"{tabla} X {contador} = {resultado}")
print("Fin de la tabla")

#EJEMPLO FOR con lista

nombres =["Jose", "M Mar","Lucia","Eva"]
for nombre in nombres:
    print(f"Hola, {nombre}")
    
#MOSTRAR 100 NUMEROS

for numero in range(100):
    print(numero+1)


  