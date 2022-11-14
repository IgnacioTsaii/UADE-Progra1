
def leerentero(mensaje, minimo, maximo, aceptasalida):
    n = int(input(mensaje))
    while n<minimo or n>maximo:
        if n==-1 and aceptasalida:  # Si se acepta el -1, salimos
            break
        print("Valor inválido. Debe estar entre", minimo, "y", maximo)
        n = int(input(mensaje))
    return n

def leerpacientes():
    lu = []  # listaurgencias
    lt = []  # listaturnos
    afiliado = leerentero("\nNúmero de afiliado? (-1 para terminar): ", 1000, 9999, True)
    while afiliado != -1:
        ta = leerentero("\nTipo de atención (0: Urgencia - 1: Con turno): ", 0, 1, False)
        if ta==0:
            lu.append(afiliado)
        else:
            lt.append(afiliado)
        afiliado = leerentero("\nNúmero de afiliado? (-1 para terminar): ", 1000, 9999, True)
    return lu, lt

# Programa principal
listaurgencias, listaturnos = leerpacientes()
print("\nPacientes atendidos con turno:")
print(*listaturnos, sep=", ")
print("\nPacientes atendidos por urgencia:")
print(*listaurgencias, sep=", ")
paciente = leerentero("\nPaciente a buscar? (-1 para terminar): ", 1000, 9999, True)
while paciente!=-1:
    print("El paciente", paciente, "fue atendido", listaturnos.count(paciente), "veces con turno y", listaurgencias.count(paciente), "por urgencias")
    paciente = leerentero("\nPaciente a buscar? (-1 para terminar): ", 1000, 9999, True)