def dameMes(num):
    meses={
        1:'enero',
        2:'febrero',
        3:'marzo',
        4:'abril',
        5:'mayo',
        6:'junio',
        7:'julio',
        8:'agosto',
        9:'septiembre',
        10:'octubre',
        11:'noviembre',
        12:'diciembre'
    }
    return  meses.get(num,'Mes no valido')

mes=int(input('introduce un numero del mes (del 1 al 12): '))
print(dameMes(mes))

#print(dameMes(3))