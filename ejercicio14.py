from datetime import datetime

actual = datetime.now().time()
print(actual)
hora_salida=19
minuto_salida=30
if (hora_salida == actual.hour) and (minuto_salida == actual.minute):
    print('ya puedes salir')
else:
    falta_horas = hora_salida - actual.hour
    falta_minutos = minuto_salida - actual.minute
    print(f'quedan {falta_horas} horas y {falta_minutos} minutos')