'''
Crie um programa que pergunte dois números ao usuário.
Em seguida o programa deverá somar os dois números e
apresentar o resultado se o valor for maior que 10
'''
num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

som = num1 + num2

if (som > 10):
    print(f"O resultado da soma dos números apresuntados é:{som}")

print(f"FIM DO PROGRAMA")


