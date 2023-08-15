'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas
'''

num1 = int(input("Informe um número inteiro de 3 algarismos: "))

if num1 > 99 and num1 < 1000:
    print(f"O algarismo da centena no numero {num1} é: {num1//100}")
else:
    print("Por favor, insira um númeo de 3 algarismos")