listaVacia = []

def calcularCuadrado(lista):
    ultimo = int(input('Ingrese hasta que ultimo valor quiere que calcule el cuadrado: '))
    for i in range(ultimo):
        lista.append(i**2)
        
    return lista


listaCuadrados = calcularCuadrado(listaVacia)
print(listaCuadrados)
for i in range(-1,-11,-1):
    print(listaCuadrados[i])