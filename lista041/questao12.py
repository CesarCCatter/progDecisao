num1 = int(input("Informe um número inteiro"))
num2 = int(input("Informe outro número inteiro"))
num3 = int(input("Informe outro número inteiro"))
num4 = int(input("Informe outro número inteiro"))
num5 = int(input("Informe outro número inteiro"))

mai = num1

if ( mai < num2 ):
    mai = num2

if ( mai < num3 ):
    mai = num3

if ( mai < num4 ):
    mai = num4

if ( mai < num5 ):
    mai = num5

men = num1

if (men > num2):
    men = num2

if (men > num3):
    men = num3

if (men > num4):
    men = num4

if (men > num5):
    men = num5

print(f"O maior valor inserido foi {mai}")
print(f"O menor valor inserido foi {men}")