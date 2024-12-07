'''Crie duas variaveis com dois valores numerics inteiros digitados pelo usuario,
caso o valor do primeiro numero for maior que o do segundo, exiba em tela uma
mensagem de acordo, caso contrario, exiba em tela uma mensagem dizendo que o
primeiro valor digitado é menor que o segundo'''

numero1 = int(input('Digite o primeiro numero:'))
numero2 = int(input('Digite o segundo numero:'))

if numero1 > numero2:
    print('O primeiro valor digitado é o maior!')
else:
    print('O segundo valor digitado é o maior!')