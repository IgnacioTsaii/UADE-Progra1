import random

def crear_tablero(num):
    # Crea mi primera matriz vacia
    matriz = [[' ' for fila in range(num)] for columna in range(num)]
    return matriz 
        
def tesoro(matriz):
    # Ubica el tesoro de manera aleatoria
    fila = random.randint(0, len(matriz) - 1)
    columna = random.randint(0, len(matriz[0]) - 1)
    matriz[fila][columna] = 'X'
    return matriz

def imprimir_tablero(matriz):
    #imprime el tablero con la X para que el usuario intente adivinar
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print()
        
def encontrar_tesoro(matriz, fila, columna):
    # Compara las coordenadas del usuario con el tesoro
    if matriz[fila][columna] == 'X':
        return True
    else:
        return False

def tesoro_escondido():
    while True:
        num = int(input("Ingrese de que tamaño quiere el tablero (NxN): "))
        if num <= 0:
            print("Error no se pueden ingresar números negativos")
        else:
            break
    
    # Creacion del tablero
    juego = crear_tablero(num)
    print("¡Bienvenido al juego del Tesoro Escondido!")
    
    # Crear el tesoro escondido e imprimir
    escondido = tesoro(juego)
    imprimir_tablero(escondido)
    
    # Adivinar la ubicacion del tesoro
    intentos = 0
    while True:
        fila = int(input("Ingresa el número de fila: "))
        columna = int(input("Ingresa el número de columna: "))
        if 0 <= fila < num and 0 <= columna < num:
            print ("Recordar que las coordenadas de la matriz van desde el 0 hasta {}".format(num-1))
            if encontrar_tesoro(escondido, fila, columna):
                print("¡Felicitaciones! Has encontrado el tesoro. En el intento número {} !!".format(intentos + 1))
                break
            else:
                print("Todavia no encontraste la ubicación del tesoro ¡Seguí intentándolo!")
        else:
            print("Por favor, ingresa valores válidos para fila y columna.")
        intentos += 1
            

# Main
tesoro_escondido()
