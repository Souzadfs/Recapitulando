# Escreva uma função que receba uma lista de números e retorne a soma dos números da lista.
def somalist (numeros):
    soma = 0

    for num in numeros:
        soma += num

    return soma

lista =[1,23,45,67,2,57]

resultado = somalist(lista)

print(resultado)