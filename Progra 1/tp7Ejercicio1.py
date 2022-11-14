def cantdigitos(n):
    if n < 0:
        n=-n 
    if n < 10: 
        return 1
    elif n >= 10: 
        return 1 + cantdigitos(n//10)

n=int(input("Ingrese un número entero: "))
print(f"La cantidad de dígitos que tiene {n} es: {cantdigitos(n)}")