#REVISÃO
#Crie um algoritmo que leia um núemro e diga se ele é par ou ímpar. Ao digitar -99 o programa deve encerrar

numero = 0
while numero != -99:
    numero = int(input('Digite um número ou -99 para sair: '))
    if numero % 2 == 0:
        print('É par')
    elif numero != -99:
        print('É impar')


