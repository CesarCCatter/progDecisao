'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
'''

nt1 = float(input("Informe a primeria nota: "))
nt2 = float(input("Informe a segunda nota: "))
nt3 = float(input("Informe a terceira nota: "))
nt4 = float(input("Informe a quarta nota: "))
med = (nt1 + nt2 + nt3 + nt4) /4

if ( med >= 5 ):
    print(f"A média do aluno foi de {med} O aluno foi aprovado, parabéns")

else:
    print(f"A média do aluno foi {med}. O aluno infelismente foi reprovado")