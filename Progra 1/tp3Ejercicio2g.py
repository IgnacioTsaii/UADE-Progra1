# dimensión
n = 0
n = int(input('Ingrese el valor de n para determinar la dimension de la matriz NxN: '))
# Genere una matriz bidimensional inicial, rellena con 0
matriz = [[0 for i in range(n)] for j in range(n)]
#nivel
nivel = 0
#posición actual
posicion = 0
while posicion < n * n:
    # Cada capa se divide en 4 grupos uniformemente, y el número de cada grupo en el número de capa actual
    num = n - (nivel * 2) - 1
    temPos = posicion

    for i in range(num):
        # temPos es el valor del primer grupo del bucle actual, y los otros 3 tiempos se calculan de acuerdo con el tamaño de paso num para el llenado
        temPos += 1
        matriz[nivel][i+nivel] = temPos

        matriz[nivel+i][n-nivel-1] = temPos + num

        matriz[n-nivel-1][n-nivel-i-1] = temPos + num * 2

        matriz[n-nivel-i-1][nivel] = temPos + num * 3
        #Para números impares, procesamiento especial una vez
        if num == 2:
            matriz[n-nivel-i-1][nivel+1] = temPos + num * 3 + 1
            posicion += 1

    nivel += 1
    posicion += num * 4

#Imprimir 
for i in matriz:
    for j in i:
        print('%5s' %j, end='')
    print("")