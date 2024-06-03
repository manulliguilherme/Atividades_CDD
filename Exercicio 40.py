#Escreva um codigo que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor,
#calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada
#escrever a média da turma e o resultado da contagem

turma = 0
soma = 0
aprovados = 0
notas = ['', '', '', '', '']
for contador in range(0, len(notas), 1): #A nota precisa vim para esse contador
    notas[contador] = float(input('Digite a notas: '))

for contador1 in range(0,len(notas), 1):
    print('notas', contador1+1, "é", notas[contador1])  #Está explicando que o 1 aluno tem a 1 nota
    soma = soma  + notas[contador1]
print("A soma das notas da turma é : ", soma)

media = soma / len(notas)
print('A média da turma é:  ', media)

for contador2 in range(0, len(notas), 1):
    if notas[contador2] >= media:
        aprovados = aprovados + 1

print("A quantidade de alunos aprovados é: ", aprovados)






