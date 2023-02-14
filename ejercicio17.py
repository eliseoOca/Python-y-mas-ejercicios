usuario=input('dame una lista de colores separados por comas: ')
usuario=set(usuario.split(','))
colore=[]
for color in usuario:
    colore.append(color)
colore.sort()
print(colore)
