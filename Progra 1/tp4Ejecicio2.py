def centrarCadena(cadena,letras):
    longitudTotal = 80
    espacios = longitudTotal - letras
    espaciosAgregar = espacios//2
    centrado = (" " * espaciosAgregar)+cadena+ " "*espaciosAgregar
    print(centrado)
    

frase = input('Ingrese la cadena que desee centrar: ')
palabras = frase.split()
longitud = len(frase)
fraseCentrada = centrarCadena(frase,longitud)
frase = frase.center(80, " ")
print(frase)