#Criar um array tamanho 5 e preencher com os nomes dos 5 alunos, informados pelo usuário. Sendo que
#agora mostre todos

nome = ['','','','','']

for contador in range (len(nome)):
    nome[contador] = input('Digite um nome: ')
for contador2 in range(len(nome)):
    print(contador2,nome[contador2],end = " ")