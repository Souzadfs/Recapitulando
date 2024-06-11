#Crie uma lista com 10 números aleatórios e escreva um loop que imprima apenas os números pares dessa lista.

import random

numeros = [random.randint(1, 100) for _ in range (10)]

print(f'Lista de numeros {numeros}')

for num in numeros:
    if num %2 == 0:
        print(f'Os numeros pares são: {num}')

for num in numeros:
    if num %2 != 0:
        print(f'Os números impares são: {num}')    