import random 
def cargarLista (lista):
    lista =[]
    for i in range (1,6):
        lista.append(random.randint(0,50))
    return lista

lista1 = []
lista2 = []

listaCargada1 = cargarLista (lista1) 
listaCargada2 = cargarLista (lista2)
print('Esta es la lista creada: ')
print(listaCargada1)
print(listaCargada2)
print('Esta es la lista intercalada: ')
intercalada = listaCargada1 + listaCargada2 
# Sumo la lista para tener una lista de ese largo
intercalada[::2] = listaCargada1
# en la lista sumada, igualo la lista 1 para que en esas posiciones me de el numero correspondiente saltando de dos en dos 
intercalada[1::2] = listaCargada2
# hago lo mismo que con la lista 1 solo que empiezo desde la posicion 1 y vaya de dos en dos
print(intercalada)