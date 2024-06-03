#Ler o nome de 2 times e o número de gols marcados na partida escrever o nome do vencedor.
# Caso não haja vencedor, deverá ser impressa a palavra empate

time1= input('Digite o nome do primeiro time:')
gol1= int(input('Digite o número de gols feito pelo primeiro time:'))
time2= input('Digite o nome do segundo time:')
gol2= int(input('Digite o número de gols feito pelo segundo time:'))

if gol1 == gol2:
    print("O", time1, "e", time2, "empataram")
elif gol1 < gol2:
    print(" O time", time2, "é o vencedor")
else:
    print(" O time", time1, "é o vencedor")