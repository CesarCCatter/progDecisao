'''
9) Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo
'''

num = int(input("Informe um número: "))

if (num > 0):
    print(f"O valor {num} inserido é positivo")
elif (num < 0):
    print(f"O valor {num} inserido é negativo")
else:
    print(f"O valor {num} inserido é neutro")
