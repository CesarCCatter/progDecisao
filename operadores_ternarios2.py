'''
Crie um programa que pergunte a idade do usuário
e em seguida informe se este usuário é menor de idade ou maior de idade
'''

idade = int(input("Informe sua idade: "))

#var = resultado_verdadeiro if teste condicional else resultado_falso

resposta = "Você é maior de idade" if idade>= 18 else "Você é menor de idade"

print(resposta)