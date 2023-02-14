def mayorEdad():
    edad= int(input('Dime tu edad: '))
    if edad> 18:
        return True
    else:
        return False
    
mayorEdad=mayorEdad()
if mayorEdad:
    print('mayor de edad')
else:
    print('menor de edad')