# Peça para o usuario digite um numero, em seguida exiba em tela uma mensagem dizendo se é par ou impar

numero1 = int(input('Digite um valor:'))
if (numero1 % 2) == 0:
    print(f'{numero1} é PAR')
else:
    print(f'{numero1} é IMPAR')