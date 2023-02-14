def baseTriangulo(base,altura):
    area = (base*altura)/2
    return area


base=float(input('ingresar base del triangulo: '))
altura=float(input('ingresar altura de triangulo: '))
area = baseTriangulo(base, altura)
print(f'el area del triangulo con base {base} y altura {altura} es {area}')