#Desafio com dois FOR

numero = int(input('Digite um número: '))
for contador in range(1, numero + 1, 1):
    for contador1 in range(0, contador, 1):
        print(contador, end = ' ')
    print()