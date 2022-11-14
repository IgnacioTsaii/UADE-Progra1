import random 
def matrizAleatoria(n,m):
    matriz = []
    for i in range(n):
        lista = []
        for j in range(m):
            lista.append(random.randint(0,151))
        matriz.append(lista)    

    return matriz

def printMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='\t')   
        print()     

def mostrarMatriz(matriz):
    for fila in matriz:
        print(fila)


m=7
n= int(input('Ingrese la cantidad de fabrias que tiene: '))

# Punto A
ma = matrizAleatoria(n,m)
printMatriz(ma)
# Punto B

filas = len(ma)
columnas = len(ma[0])
suma = 0

for i in range(filas):
    suma = sum(ma[i])
    matriz[i].append(suma)

mostrarMatriz(ma)

for i in range(num):
    for j in range(num):
        print(matriz[i][j], end='\t')
    print() 