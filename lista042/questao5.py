'''
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

sigl = input("Informe a sigla de um estado: ")

if (sigl == "RJ" or sigl == "SP" or sigl == "ES" == sigl == "Mg"):
    print(f"O estado {sigl} está na região Sudeste.")

else:
    print(f"O estado {sigl} não pertence a região Sudeste ou foi escrito de maneira incorreta.")
