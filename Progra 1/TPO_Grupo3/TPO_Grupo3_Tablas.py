import random

def matrizAleatoria(n,m):
    matriz = []
    algo=0
    for i in range(n):
        lista = []
        for j in range(m):
            lista.append(palabraMatriz[algo])
            algo +=1
        matriz.append(lista)    

    return matriz

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print((matriz[i][j]).center(10, " "), end='\t')   
        print()     

def buscaPosicion():
    claveDicc= {
        'GRABE':[0,0],
        'GRAVE':[0,1],
        'BELLO':[1,0],
        'VELLO':[1,1],
        'HAY':[2,0],
        'AHÍ':[2,1]
        }
    
    claveList=['GRABE', 'GRAVE', 'BELLO', 'VELLO', 'HAY', 'AHÍ']
    
    azar = random.choice(claveList)
    a = claveDicc.get(azar)
    return azar,a

def palabraClave(pos,matriz):
    if pos == [0,0]:
        pos = matriz[0][0]
    elif pos ==[0,1]:
        pos =matriz[0][1]
    elif pos ==[1,0]:
        pos =matriz[1][0]
    elif pos ==[1,1]:
        pos =matriz[1][1]
    elif pos ==[2,0]:
        pos =matriz[2][0]
    elif pos ==[2,1]:
        pos =matriz[2][1]    
    
    return pos

palabraMatriz = ['hola', 'ola', 'asta', 'hasta', 'honda', 'onda', 'baya', 'valla', 'vaya', 'blanco']
random.shuffle(palabraMatriz)
buscador = buscaPosicion()

print(buscador[0].center(13, " ")) #Como me devolvio una Tupla
ma = matrizAleatoria(3,2)
printMatriz(ma)
posicion = posicionPalabraClave(buscador[1],ma)
print()
contraseña = palabraRespuesta(posicion)
respuesta = input('Ingrese su palabra clave: ')
contador +=1
while respuesta != contraseña:
    print('Error - intente de nuevo')
    respuesta = input('Ingrese su palabra clave: ')
    contador +=1
