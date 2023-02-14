#tabla de multiplicar
tabla=int(input("Que tabla quieres calcular?"))
#creamos la variable contador
contador=1
print(f"Tabla del {tabla}")
#bucle o repeticion
while (contador<11):
    resultado=tabla*contador
    #mostramos la tabla
    print(f"{tabla} por {contador} es igual a {resultado}\n")
    #comprobamos si vale 4 y salimos
    if contador==4:
        print("El contador es igual a 4 y no continuo")
        break
    #incrementamos el contador
    contador=contador+1
print("fin de la tabla")