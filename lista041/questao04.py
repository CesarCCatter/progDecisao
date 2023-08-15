'''
4) Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Informe um número "))

if ((num % 4 == 0 ) and (num % 5 == 0)):
    print(f"O resultado da divisão por 4 é: {num / 4}, e o resultado da divisão por 5 é: {num / 5} ")
else:
    print("O valor não é divisível por 4 e 5")