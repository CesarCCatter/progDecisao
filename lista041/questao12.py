'''
12) Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número.
'''

num1 = int(input("Por favor, informe um número"))
num2 = int(input("Por favor, informe outro número"))
num3 = int(input("Por favor, informe outro número"))
num4 = int(input("Por favor, informe outro número"))
num5 = int(input("Por favor, informe outro número"))

mai = num1

if (mai < num2):
    mai = num2

elif (mai < num3):
    mai = num3

elif(mai < num4):
    mai = num4

elif ( mai < num5):
    mai = num5

men = num1

if (men > num2):
    men = num2

elif (men > num3):
    men = num3

elif(men > num4):
    men = num4

elif ( men > num5):
    men = num5

    print(f"O menor número inserido é: {men}")
    print(f"O maior número inserido é: {mai}")

