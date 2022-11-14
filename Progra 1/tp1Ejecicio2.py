def concatenarNumeros (a,b):
    cantcifras = 0
    copiaB = b
    while copiaB >0:
        copiaB = copiaB//10
        cantcifras +=1

    paraUnir = 10**cantcifras
    paraSumar = paraUnir*a
    resultado = paraSumar + b
    return resultado

num1 = int(input('Ingrese el primer numero: '))    
num2 = int(input('Ingrese el segundo numero: '))    
concatenarNumeros(num1, num2)