'''
7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

num1 = input("Informe um número: ")
num2 = input("Informe outro número:  ")

if (num1 > num2):
    print(f"O maior número é: {num1}")
elif (num2 > num1):
    print(f"O maior número é: {num2}")
else:
    print("Ambos os números são iguais")