'''
10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
'''

nome = input("Iforme o nome do aluno: ")

nt1 = float(input("Informe a nota do aluno na prova 1: "))
nt2 = float(input("Informe a nota do aluno na prova 2: "))
media = (nt1 + nt2) /2

if ( media < 3 ):
    print( "O aluno infelismente foi reprovado.")
elif ( media < 7 ):
    print("O aluno está em prova final.")
else:
    print("O aluno foi aprovado, parabéns!")
