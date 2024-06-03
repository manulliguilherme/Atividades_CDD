#REVISAO
#Crie um menu para que o usuário escolha fazer um dos cálculos, e tenha a opção 3 para sair
pergunta = 0

while pergunta != 3:
    pergunta = int(input("Escolha uma opção: \n"  "1- Calculo do triângulo\n" "2- Cálculo do quadrado\n" "3- Sair do programa \n  "))
    if pergunta == 1:
        base = float(input('Digite o valor da base do triângulo: '))
        altura = float(input('Digite o valor da altura do triângulo: '))
        areat = (base * altura) / 2
        print(f"A área do triângulo é: {areat} ")
    elif pergunta == 2:
        lado = float(input('Digite o lado do quadrado:  '))
        areaq = lado ** 2
        print(f"A área do quadrado é {areaq}")
    elif pergunta == 3:
        print('Saindo...')
    else:
        pergunta = int(input("Número inválido.\n As opções são:\n 1- Calculo do triângulo\n 2- Cálculo do quadrado\n 3- Sair do programa\n  "))


