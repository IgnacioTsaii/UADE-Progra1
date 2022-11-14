def buscarmayor (x):
    mayor = -1
    copiaMayor = 0
    if x == copiaMayor:
        copiaMayor = mayor
    return copiaMayor

    if x > copiaMayor:
        copiaMayor = x

    return mayor

# Programa principal
cont = 0
while cont != 3:
    num = int(input('Ingrese 3 numeros: '))
    if num <= 0:
        print('El numero que ingreso es invalido')
    else:
        buscarmayor(num)
        cont += 1
