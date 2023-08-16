'''
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Informe um número de 1 a 7: "))

if (num ==1):
    print(f"O número da semana correspondente ao número {num} é: Domingo")
elif (num ==2):
    print(f"O número da semana correspondente ao número {num} é: Segunda-feira")
elif (num ==3):
    print(f"O número da semana correspondente ao número {num} é: Terça-feira")
elif (num ==4):
    print(f"O número da semana correspondente ao número {num} é: Quarta-feira")
elif (num == 5 ):
    print(f"O número da semana correspondente ao número {num} é: Quinta-feira")
elif (num == 6):
    print(f"O número da semana correspondente ao número {num} é: Sexta-feira")
elif (num == 7):
    print(f"O número da semana correspondente ao número {num} é: Sabado")
else:
    print("Número inválido")