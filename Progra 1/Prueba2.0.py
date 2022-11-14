import random

alfabeto = ['a','b','c','d','e','f','g','h']
matrizAlfa = [None] * 5
for i in range(0,5):
    matrizAlfa[i] = [None] *5
    
for i in range(0,5):
    for j in range(0,5):
        matrizAlfa[i][j] = alfabeto[random.randint(0,7)]

print(matrizAlfa)


print(matrizAlfa[2][4])