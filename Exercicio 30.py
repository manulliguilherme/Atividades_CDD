#Escreva um código para ler as notas 1a e 2a avaliações de um aluno, calcule e imprima a média desse aluno.
#Só devem ser aceitos valores váçidos, durante a leitura, (0 a 10) para cada nota

nota1 = float(input('Digite a primeira nota: '))

while nota1 <0 or nota1 > 10:
    nota1 = float(input('Nota não aceita. Digite a primeira nota novamente: '))


nota2 = float(input('Digite a segunda nota: '))

while nota2 < 0 or nota2 >10:
    nota2 = float(input('Nota não aceita. Digite a segunda nota novamente: '))

soma = nota1 + nota2
media = soma / 2

print(f"A média do aluno é {media}")

