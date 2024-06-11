#Crie um programa que pergunte ao usuário seu nome e idade, e então imprima uma mensagem personalizada.

name = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))
idademax = 20

if idade  >= idademax:
    print(f'Olá {name}, sua idade é {idade} anos, então poderá participar conosco')

else:
    print(f'Olá {name}, sua idade é inferior a {idademax}, e infelizmente não poderá participar conosco')    

