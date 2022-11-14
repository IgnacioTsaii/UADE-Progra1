"""Escribir un programa para rellenar e imprimir una matriz de enteros de N x N con los
números del 1 al 4, respetando el patrón por cuadrantes detallado más abajo. El pro-
grama debe servir para cualquier valor par de N, el que se ingresa por teclado."""
def rellenarmatriz(matriz):
    fila=len(matriz)
    columna=len(matriz[0])
    fila1=0
    columna1=0
    mitadfila=fila//2 #hasta la mitad de la fila se imprime un numero
    mitadcolumna=columna//2 #hasta la mitad de la columna se imprime otro
    cont1=1
    cont2=2
    cont3=3
    cont4=4 
  
    for f in range(fila1,mitadfila):
        for c in range(columna1,mitadcolumna):
            matriz[f][c]=cont1
    for f in range(fila1,mitadfila):
        for c in range(mitadcolumna,columna):
            matriz[f][c]=cont2
    for f in range(mitadcolumna,fila):
        for c in range(columna1,mitadcolumna):
            matriz[f][c]=cont3
    for f in range(mitadcolumna,fila):
        for c in range(mitadcolumna,columna):
            matriz[f][c]=cont4
    return matriz

def imprimirmatriz(matriz):
    fila=len(matriz)
    columna=(len(matriz[0]))
    for f in range(fila):
        for c in range(columna):
            print("%3d" %matriz[f][c], end="")
        print()
    return matriz

size=int(input("Ingrese el tamaño de la matriz: "))
while size %2 != 0:
    size=int(input("Ingrese un numero par para el tamaño de la matriz: "))
matriz=[[0]*size for i in range(size)]
rellenarmatriz(matriz)
imprimirmatriz(matriz)
