#ejercicio 2
import random
arregloA=[]
for _ in range(10):
    numero_aleatorio= random.randint(0,500)
    arregloA.append(numero_aleatorio)
    if numero_aleatorio % 2 == 0:
     print(numero_aleatorio)


