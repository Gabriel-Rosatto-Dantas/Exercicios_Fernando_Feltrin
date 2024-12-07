'''Crie um programa que realiza a progressão ariymetica de 20 elementos,
 com primeiro termo e ração defenidos pelo usuario'''
 
valor = int(input('Digite o valor:'))
razao = int(input('Digite a razão da progressão:'))

pa = valor + (20 - 1) * razao

for i in range(valor, pa + razao, razao):
    print(i)