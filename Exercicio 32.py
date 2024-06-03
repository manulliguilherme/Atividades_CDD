#Perguntar quantos alunos tem na sala, e pedir a nota de cada um a quantidade de vezes
#que tem na sala

somamedia = 0

alunos = int(input('Quantos alunos tem na sala? '))
for x in range(1, alunos+1, 1):
    nota1 = float(input('Digite a primeira nota do aluno: '))
    while nota1 <0 or nota1 > 10:
        nota1 = float(input('Nota não aceita. Digite a primeira nota novamente: '))

    nota2 = float(input('Digite a segunda nota do aluno: '))
    while nota2 < 0 or nota2 >10:
        nota2 = float(input('Nota não aceita. Digite a segunda nota novamente: '))

    media = (nota1 + nota2)/2
    print(media)
    somamedia = somamedia + media

media = somamedia / alunos
print(f"A média do aluno é {media}")

