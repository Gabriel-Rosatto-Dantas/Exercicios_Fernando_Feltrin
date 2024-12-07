'''Crie um programa que realiza a contagem de 1 até 100, usando números impares,
ao final do processo exiba em tela quantos numeros ímpares foram encontrados nesse
intevalo, assim como a soma dos mesmos'''

contagem = 0
soma = 0

for i in range(1, 101):
    if i % 3 == 0:
        soma += i
        contagem += 1

print(f"Contagem de números ímpares: {contagem}")
print(f"Soma dos números ímpares:{soma}")

