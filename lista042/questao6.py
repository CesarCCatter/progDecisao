'''
6. Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos."
'''

ann = int(input("Informe o seu ano de nascimento: "))
ana = int(input("Informe o ano atual: "))
idd = ana - ann


#var = resultado_verdadeiro if teste condicional else resultado_falso
resposta = f"A sua idade é: {idd}" if (idd >= 0) else "Os dados inseridos estão incorretos"

print(resposta)


