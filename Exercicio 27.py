#Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas desses
# alunos no final mostre a média aritmétrica da turma

alunos = 0
soma = 0

pessoas = int(input('Quantos alunos tem na sala? '))
while alunos < pessoas:
    nota = float(input('Digite uma nota para cada aluno dessa sala: '))
    soma = soma + nota
    alunos = alunos + 1

media = soma / alunos

print(f"A soma é: {soma}, a quantidade de alunos é: {alunos}, a média é: {media}")