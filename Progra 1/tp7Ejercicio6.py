def A(m,n):
    if m==0:
        return n+1
        
    elif n==0:
        return A(m-1,1)
    
    else:
        return A(m-1,A(m,n-1))

#Programa Principal
    # Cuadro: Filas deben ser M y las columnas N

for i in range(3):
    for j in range(7):
        print("%4d"%A(i,j),end="")  
    print()