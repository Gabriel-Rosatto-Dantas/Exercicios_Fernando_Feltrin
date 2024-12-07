'''Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuario'''

numero = int(input('Digite um número:'))
for i in range(1, 11):
    print(f'{numero} X {i} = {i * numero}')