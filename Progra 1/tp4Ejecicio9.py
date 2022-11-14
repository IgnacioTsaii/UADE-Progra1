def ultimosValores(cadena,cantidad):
    print(cadena[-cantidad:])

frase = input('Ingrese una oración: ')
longitud = int(input('Que ultimos valores quiere imprimir? '))
palabras = frase.split()
ultimosValores(frase,longitud)