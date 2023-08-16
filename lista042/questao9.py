'''
9. Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

idd = int(input("Informe um número: "))

if ( idd < 18 ):
    print("Você é menor de idade")
elif ( idd > 17 ):
    print("Você é maior de idade")
elif (idd > 65):
    print("Você tem mais de 65 anos")