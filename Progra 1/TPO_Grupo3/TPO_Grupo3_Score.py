def grabarPuntuacion(intentos=4, fallos=1):
        arch = open('Registros.txt', 'at')
        nombre = input('Ingrese el nombre del usuario: ')
        arch.write(nombre+',')
        arch.write('Intentos: %s ' %intentos)
        arch.write('- Fallos: %s' %fallos + '\n')
        
        arch.close()
    
score = grabarPuntuacion()
