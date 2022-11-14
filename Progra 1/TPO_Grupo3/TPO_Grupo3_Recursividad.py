import random

def generarVoltaje():
    voltaje = []
    for i in range (10):
        voltaje.append(random.randint(1,120))
    return voltaje

def buscarMayor(listaVoltaje, inicio=0):
    if inicio<len(listaVoltaje)-1:
        actual = listaVoltaje[inicio]
        mayor = buscarMayor(listaVoltaje,inicio+1)
        return actual if actual>mayor else mayor
    else:
        return listaVoltaje[-1]

def buscarMenor(listaVoltaje, inicio=0):
    if inicio<len(listaVoltaje)-1:
        actual = listaVoltaje[inicio]
        menor = buscarMenor(listaVoltaje,inicio+1)
        return actual if actual<menor else menor
    else:
        return listaVoltaje[-1]


def imprimirLista(listaVoltaje,inicio=0):
    if inicio<len(listaVoltaje):
        print(listaVoltaje[inicio], end=' ')
        imprimirLista(listaVoltaje, inicio+1)



vol = generarVoltaje()
imprimirLista(vol)
print()
maximo = buscarMayor(vol)
print('este es el mas grande', maximo)
print()
minimo = buscarMenor(vol)
print('este es el mas chico', minimo)