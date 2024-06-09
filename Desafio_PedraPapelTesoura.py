contador1 = 0
contador2 = 0
for contador in range(0,3,1):
    jogador1 = int(input(f" \n Jogador 1, escolha uma dessas opções: \n"
                         f" 1- Pedra \n"
                         f" 2- Papel \n"
                         f" 3- Tesoura \n"
                         f" --> "))
    jogador2 = int(input(f" \n Jogador 2, escolha uma dessas opções: \n"
                         f" 1- Pedra \n"
                         f" 2- Papel \n"
                         f" 3- Tesoura \n"
                         f" --> "))

    if jogador1 == 1 and jogador2 == 3 or jogador1 == 2 and jogador2 == 1 or jogador1 == 3 and jogador2 == 2:
        print(f" O Jogador 1 venceu!")
        contador1 += 1
    elif jogador2 == 1 and jogador1 == 3 or jogador2 == 2 and jogador1 == 1 or jogador2 == 3 and jogador1 == 2:
        print(f" O Jogador 2 venceu!")
        contador2 += 1
    else:
        print("Empate!")

    if contador1 == 2 or contador2 == 2 and contador < 2:
        print("Não tem chance de virada!")
        break

print(f" \n PLACAR FINAL: \n"
    f"Jogador 1 = {contador1} \n"
    f"Jogador 2 = {contador2} \n")