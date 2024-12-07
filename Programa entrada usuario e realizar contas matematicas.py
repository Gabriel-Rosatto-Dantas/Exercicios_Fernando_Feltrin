'''Escreva um programa que pede que o usuario de entrada em dois valores,
em seguida, exiba em tela o resultado da soma, subtração, multiplicação e
divisão desses números'''

numero1 = int(input('Digite o primeiro valor:'))
numero2 = int(input('Digite o segundo valor:'))

resultado_soma = numero1 + numero2
resultado_subtracao = numero1 - numero2
resultado_multiplicacao = numero1 * numero2
resultado_divisao = numero1 / numero2
    
print(f'A soma dos números informados é {resultado_soma}')
print(f'A subtração dos números informados é {resultado_subtracao}')
print(f'A multiplicação dos números informados é {resultado_multiplicacao}')
print(f'A divisão dos números informados é {resultado_divisao}')