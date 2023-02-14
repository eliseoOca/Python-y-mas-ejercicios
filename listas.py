
lista = [1,2.3, 'eliseo',[7,8],12]
print(type(lista))
print(lista)


print(lista[2])
print(lista[3][1])
print(lista[1:4])
print(lista[2:4:2])

for elemento in lista:
    print(elemento)
    
lista.append(10)
lista.append('fernando')
lista.append([2,3,6,8,9])
print(lista)
lista.extend([4,5,2,4])
print(lista)
lista.remove(2)
lista.remove('fernando')
print(lista)

print(lista.index('eliseo'))
print(lista.count(4))
print(lista)

lista.reverse()
print(lista)

#mas ejemplos
listaCompra=['pan','batatas','naranjas','kiwis']
print(listaCompra)

#crear una lista desde variables
catidadPan=5
precioPan=0.40
total=catidadPan*precioPan
pedido01=[catidadPan,precioPan,total]
pedido02=[3,0.60,3*0.60]
pedido03=[4,0.50,4*0.50]
pedidos=[pedido01,pedido02,pedido03]
print(pedidos)

#lista vacia
listaVacia=[]
print(listaVacia)
print(type(listaVacia))
listaCompra.append("peras")
listaCompra.insert(2,'bananaas')
print(listaCompra)

listaCompra.pop()
print(listaCompra)

#longitud lista
print(len(listaCompra))

#ejemplo añadir con bucle for
cuadrados = []
for numero in range(1,11):
    cuadrados.append(numero*numero)
print(cuadrados)
print(min(cuadrados))
print(max(cuadrados))
print(sum(cuadrados))

#esa en lista
print(listaCompra)
print('bananaas' in listaCompra)
print('jamon' in listaCompra)




