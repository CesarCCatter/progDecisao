'''
10) Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe outro número inteiro: "))

if num1 % num2 == 0:
    print(f"O número {num1} é divisivel por {num2}")
else:
    print(f"O número {num1} não é divisível por {num2}.")
