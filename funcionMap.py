#funcion map
import functools
lista=[23, 56, 7, 2, 6, 9, 18, 21, 75, 65]
print(list(map((lambda valor: valor * valor), lista)))

#funcion filter

print(list(filter((lambda valor: valor % 2 ==0), lista)))

#funcion reduce
print(str(functools.reduce((lambda x, resultado: x+resultado), lista)))