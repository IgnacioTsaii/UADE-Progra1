def capicua(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False


def remover_caracteres_especiales(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    return cadena


cadena = "Isaac no ronca así"
cadena_limpia = remover_caracteres_especiales(cadena)
es_capicúa = capicua(cadena_limpia)
if es_capicúa:
    print("Es capicúa")
else:
    print("No es capicúa")