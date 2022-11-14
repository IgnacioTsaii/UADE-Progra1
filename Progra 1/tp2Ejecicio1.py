import random 
def cargarLista (lista):
    lista =[]
    for i in range(random.randint(10,99)):
        lista.append(random.randint(1000,9999))
    return lista    

def sumarLista(lista):
    suma = sum(lista)
    return suma

def eliminarElemento(lista):
    elemento = int(input('Ingrese el elemento que desea eleminar: '))
    cant = 0
    cant = lista.count(elemento)
    for i in range(cant):
        lista.remove(elemento)

    return lista

lista = []

listaCargada = cargarLista (lista)
print('Esta es la lista creada: ')
print(listaCargada)
suma = sumarLista(listaCargada)
print('La suma de los numeros de la list es: ', suma)
eliminar = eliminarElemento(listaCargada)
print(eliminar)
