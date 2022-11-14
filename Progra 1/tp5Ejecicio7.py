import random
contador = 0
while True:
    try:
        n = int(input('Adivine el número del 1 al 500: '))
        azar = random.randint(0,500)
        contador +=1
        while n != azar:
            n = int(input('Adivine el número del 1 al 500: '))
            contador +=1
    except ValueError:
        print('Dato inválido.')
        print('Intente nuevamente')
        contador +=1
    else:
        break    

print('Intentos: ', contador)
print('Número al azar: ', n)