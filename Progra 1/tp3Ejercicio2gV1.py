# dimensión
n = 0
num = int(input('Ingrese el valor de n para determinar la dimension de la matriz NxN: '))
matriz = [[0 for i in range(n)] for j in range(n)]
n=1
minimo=0
maximo=num-1
# La variable count es para saber cuantas veces tiene que hacer el cuadrado 
count = int((num+1)/2)
for i in range(count):
    # Imprimo la primera fila que iria desde la posicion (min,min) hasta (min,max+1)
    # matriz [x][y+1...]
    for j in range(minimo,maximo+1):
        matriz[i][j]=n
        n+=1
    # Imprimo lo que seria la columna derecha que esta siempre en la posicion max 
    # matriz [x+1...][y]
    for j in range(minimo+1,maximo+1):
        matriz[j][maximo]=n
        n+=1
    # Imprimo lo que seria la fila de abajo    
    # matriz [x][y-1...]  
    for j in range(maximo-1,minimo-1,-1):
        matriz[maximo][j]=n
        n+=1
    # Imprimo lo que seria la columna izq que esta en la posicion min
    # matriz [x-1...][y]
    for j in range(maximo-1,minimo,-1):
        matriz[j][minimo]=n
        n+=1      

    # Para que siga imprimiendome los datos de "adentro del cubo" declaro min+1 max-1
    minimo+=1
    maximo-=1


for i in range(num):
    for j in range(num):
        print(matriz[i][j], end='\t')
    print() 