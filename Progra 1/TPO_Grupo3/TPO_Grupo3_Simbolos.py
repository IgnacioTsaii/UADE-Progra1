import random

def generarSimbolos():
    listaSimbolos = ['☺', '╦', 'æ', '÷', '☻', '¬', '§', 'ð', '±', '¾', '«', '½', '¥', '©', 'Â', '×', '■', '~']
    azarSimbolos = []
    for i in range (3):
        azarSimbolos.append(random.choice(listaSimbolos))
    return azarSimbolos

def imprimirSimbolos(listaSimbolos,inicio=0):
    if inicio<len(listaSimbolos):
        print(listaSimbolos[inicio], end=' ')
        imprimirSimbolos(listaSimbolos, inicio+1)
    
def comparacionSimbolos(listaSimbolos,respuesta):
    while listaSimbolos != respuesta:
        respuesta.clear() #Si no lo aprendimos: respuesta = []
        print('Error - Intente nuevamente: ')
        for i in range(3):
            res = input('Ingrese los simbolos 1 a la vez, con los codigos que le indique su compañer@: ')
            respuesta.append(res)
        
simbolos = generarSimbolos()
imprimirSimbolos(simbolos)
print()
cant = 0
listaRes = []
for i in range(3):
    res = input('Ingrese los simbolos 1 a la vez, con los codigos que le indique su compañer@: ')
    listaRes.append(res)
print(listaRes)
resCorrecta = comparacionSimbolos(simbolos,listaRes)