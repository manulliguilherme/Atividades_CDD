#REVISÃO
#Crie um código que leia a idade de uma pessoa e diga em qual ano ela nasceu.

anovigente = 2024
novo = 'sim' #digitar esse como primeiro

while novo == 'sim' or novo =='S' or novo == 'Sim':
    idade = int(input('Digite a idade: '))
    aniversario = input('Você já fez aniversário? Responda com Sim ou Não.  ')
    if aniversario == 'não':
        calculo = (anovigente - idade) - 1
    else:
        calculo = anovigente - idade

    print('Você nasceu no ano de:',calculo)
    novo = input('Deseja fazer o cálculo novamente: ')
else:
    print("Fim de programa!")