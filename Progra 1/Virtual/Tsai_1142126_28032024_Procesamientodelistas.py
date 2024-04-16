def doble(lista):
    """
    Me imprime una lista con el doble de cada elemento de la lista que le doy.
    """
    return [valor * 2 for valor in lista]

def cantidadEntre(lista, desde, hasta):
    """
    Me devuelve, dentro del rango especificado, la cantidad de valores que se encuentran en la lista.
    """
    cantidad = 0
    for valor in lista:
        if desde <= valor <= hasta:
            cantidad += 1
    return cantidad

def cantidadNegativos(lista):
    """
    Me imprime la cantidad de valores negativos que contiene la lista que le doy.
    """
    cantidad = 0
    for valor in lista:
        if valor < 0:
            cantidad += 1
    return cantidad

def promedio(lista):
    """
    Imprime el contenido de la lista y me calcula el promedio de los valores.
    """
    suma_total = 0
    total_valores = 0

    for indice, valor in enumerate(lista):
        print(f"{indice} → {valor}")
        suma_total += valor
        total_valores += 1

    if total_valores > 0:
        promedio_calculado = suma_total / total_valores
        print(f"Promedio: {promedio_calculado:.2f}")


lista = [1, 1, 2, 3, 5]
lista2 = [1,-10, 2, 12, 7, 6, -5, 4]

# Función doble
resultado_doble = doble(lista)
print("Doble de cada elemento:", resultado_doble)

resultado_doble = doble(lista2)
print("Doble de cada elemento:", resultado_doble)

# Función cantidadEntre
cantidad = cantidadEntre(lista, 3, 11)
print("Cantidad entre 3 y 11:", cantidad)

cantidad = cantidadEntre(lista2, 3, 17)
print("Cantidad entre 3 y 17:", cantidad)

# Función cantidadNegativos
cantidad_neg = cantidadNegativos(lista)
print("Cantidad de valores negativos:", cantidad_neg)

cantidad_neg = cantidadNegativos(lista2)
print("Cantidad de valores negativos:", cantidad_neg)

# Función promedio
promedio(lista)
promedio(lista2)
