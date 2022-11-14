import random

def generarnumeroalazar(inf, sup):
    if sup<inf:
        inf, sup = superior, inferior  # Intercambio estilo Python
    hayrepetidos = True         # Bandera para saber si hay dígitos repetidos
    intentos = 0
    # Se establece un límite de 30 intentos para obtener un número al azar
    # sin dígitos repetidos. Esto evita ciclos infinitos en caso de ser imposible
    # obtener dicho número, por ejemplo si el intervalo fuera 440, 449.
    while hayrepetidos and intentos<30:
        hayrepetidos = False
        n = random.randint(inf, sup)
        # Descomentar la línea siguiente para comprobar el proceso
        # print("Candidato:",n)
        copia = n
        cantdigitos = [0] * 10      # Creamos una lista con 10 ceros
        while n>0:
            digito = n%10           # última cifra del número
            n//=10                  # eliminamos la última cifra
            cantdigitos[digito]+=1  # e incrementamos el contador de dígitos
        if max(cantdigitos)>1:
            hayrepetidos=True
            intentos+=1
    if intentos<30:
        return copia
    else:
        return -1

# Programa principal
inferior = int(input("Ingrese el menor número al azar que desea: "))
superior = int(input("Ingrese el menor número al azar que desea: "))
azar = generarnumeroalazar(inferior, superior)
if azar!=-1:
    print("El número obtenido es", azar)
else:
    print("No se puede generar un número al azar sin dígitos repetidos en el intervalo ingresado")
