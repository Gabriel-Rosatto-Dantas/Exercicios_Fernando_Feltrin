'''Crie um programa que lê um valor de inicio e um valor de fim, exibindo em tela
a contagem dos números  dentro desse intervalo'''

valor1 = int(input('Digite o valor inicial:'))
valor2 = int(input('Digite o valor final:'))
for valor in range(valor1,valor2 + 1):
    print(valor)