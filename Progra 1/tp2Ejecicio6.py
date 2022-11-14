import random 
def cargarLista (lista):
    lista =[]
    for i in range(random.randint(0,20)):
        lista.append(random.randint(0,10))
    return lista

def normalizarLista(lista, total):
    listaNormal = []
    porcentaje = 0
    for i in range (len(lista)):
        porcentaje = lista[i]/total
        listaNormal.append(porcentaje)
    return listaNormal    

listaVacia = []
lista1 = cargarLista(listaVacia)
totalLista1 = sum(lista1)
print(lista1)

lista2 = normalizarLista(lista1,totalLista1)
print(lista2)