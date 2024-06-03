#Faça um código para ler um vetor de 10 números. Após isso ler mais um número qualquer
#calcular e escrever quantas vezes esse número aparece no vetor


vetor = [0,0,0,0,0,0,0,0,0,0]
soma = 0

for contador in range(0, len(vetor), 1):
   vetor[contador] = float(input(f"Digite o {contador}º número: "))

repeticao = int(input('Quantas vezes você deseja  contar:'))

for contador1 in range(0, len(vetor), 1):
   if vetor[contador1] == repeticao:
       soma = soma + 1

print(f" O número {repeticao} apareceu {soma} vezes.")

