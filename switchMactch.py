color ='rojo'
match color:
    case 'rojo':
        print('es rojo')
    case 'azul':
        print('es azul')
    case 'verde':
        print('es verde')
    case _:
        print('ese color no esta aqui')
        

mes=1
match mes:
    case 1:
        print('enero')
    case 2:
        print('febrero')