'''
13) Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Informe um valor para a: "))
b = int(input("Informe um valor para b: "))
c = int(input("Informe um valor para c: "))

# 1- a tem que ser menor que b

if ( a > b ):
    aux = b
    a = b
    b = aux

# Garantido até aqui que o menor entre a e b o menor está em a

# 2- a tem que ser menor que c

if ( a > c ):
    aux = a
    a = c
    c = aux

#garantido até aqui que a é o menor dos 3
#3- b tem que ser menor que c

if ( b > c ):
    aux = b
    b = c
    c = aux


print(f"Os valores em ordem crescente é: {a, b, c}")











