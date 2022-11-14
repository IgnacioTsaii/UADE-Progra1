import random
from colorama import init,Fore

def generaCables():
    ''' Genera de forma aleatoria los cables. '''
    listaCables = []
    for i in range (4):
        listaCables.append(random.randint(1,4))
    return listaCables


def imprimirCables(cables):
    ''' Imprime las opciones en consola con sus colores. '''
    for i in range(len(cables)):
        if cables[i] == 1:
            init(autoreset=True)
            print(Fore.RED+"="*50)
        elif cables[i] == 2:
            init(autoreset=True)
            print(Fore.GREEN+"="*50)
        elif cables[i] == 3:
            init(autoreset=True)
            print(Fore.CYAN+"="*50)
        elif cables[i] == 4:
            init(autoreset=True)
            print(Fore.MAGENTA+"="*50)
         

def solCables(cables,numBomba):
    ''' Recorre la lista y genera la solucion. '''
    #El 1 es el cable ROJO
    #El 2 es el cable VERDE
    #El 3 es el cable AZUL
    #El 4 es el cable VIOLETA
    cablesRojos = cables.count(1)
    #cablesVerdes = cables.count(2)
    cablesAzules = cables.count(3)
    #cablesVioletas = cables.count(4)

    print()
    if cablesRojos >= 2 and numBomba%2 == 1:
        solucion = cables.index(1)
        solucion +=1
        return solucion
    elif cables[3] == 2 and cablesRojos == 0:
        solucion = 1
        return solucion
    elif cablesAzules == 1:
        solucion = 4
        return solucion
    else:
        solucion = 2
        return solucion


print('Bombin!')
numeroBomba = random.randint(100000,999999)
print('Nº Serial:',numeroBomba)
a = generaCables()
imprimir = imprimirCables(a)
respuestaCorrecta = solCables(a,numeroBomba)

contador = 1
respuesta = int(input('Cortar el cable número: '))
while respuesta != respuestaCorrecta:
    try:
        while respuesta != respuestaCorrecta:
            respuesta = int(input('Cortar el cable número: '))
            contador +=1
    except ValueError:
        print('Dato inválido.')
        print('Intente nuevamente')
        contador +=1
    else:
        break
fallos = contador - 1   
print('Nº Intentos:', contador)
print('Nº FALLOS:', fallos)