'''Dadas duas variaveis num1 e num2 com valores 100 e 89, verifique se num1 é maior que num2
Verifique se os valores são iguais
Verifique se os valores são diferentes
Verifique se os valores num1 é igual ou menos que 100
Verifique se os valores de num1 e de num2 são iguais ou menores que 100
Verifique se os valores de num1 ou de num2 são iguais ou maiores que 100
Verifique se o valor de num1 consta nos elementos da lista1. Sendo num1=100 e lista1 = [10,100,1000,10000,100000]'''


num1 = 100
num2 = 89

print(num1 > num2)
print(num1 == num2)
print(num1 != num2)
print(num1 <= 100)
print(num1 <=100 and num2 <= 100)
print(num1 >= 100 or num2 >= 100)

lista1 = [10,100,1000,10000,100000]
print(num1 in lista1)
