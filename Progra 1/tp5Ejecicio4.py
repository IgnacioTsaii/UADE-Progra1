contador = 1
while True and contador != 100000:
    try:
        print(contador, end=' ')
        contador += 1
    except KeyboardInterrupt:
        frenar = input('Desea frenar el programa ? (S/N)')
        if frenar.upper() == 'S':
            break