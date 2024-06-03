#REVISÃO
#Escreva um algoritmo para ler a hora de inicio e a hora de fim de um jogo de xadrez (considere apenas horas inteiras,
# sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que
#o jogo pode iniciar em um dia e terminar no dia seguinte


comeco = int(input('A que horas começou o jogo de xadrez: '))
final = int(input('A que horas terminou o jogo de xadrez: '))

if comeco < final:
    total = final - comeco
    print(total)
else:
    total = (24 - comeco) + final
    print(f"O total de horas do jogo de xadrez: {total} horas")

