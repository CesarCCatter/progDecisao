'''
6) Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

if (num1 > num2):
    print(f"O resultado da subtração do maior valor pelo menor valor é: {num1 - num2}")

else:
    print(f"O resultado da subtração do maior valor pelo menor valor é: {num2 - num1}")
