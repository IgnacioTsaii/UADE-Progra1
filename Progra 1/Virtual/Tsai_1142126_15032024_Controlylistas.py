lista_resultado = []

lista1 = ["Hola", "nombre", "Ignacio", "Tsai"]
lista2 = ["mi", "es"]

longi_lista1 = len(lista1)
longi_lista2 = len(lista2)

# Elijo la lista mas larga
longi_maxima = max(longi_lista1, longi_lista2)

for i in range(longi_maxima):
    if i < longi_lista1:
        lista_resultado.append(lista1[i])
    if i < longi_lista2:
        lista_resultado.append(lista2[i])

print("Lista resultado:", lista_resultado)
