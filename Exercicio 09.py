#Faça um código que receba 3 notas de um aluno e verifique se ele está aprovado, reprovado ou
#em recuperação

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("Sua média é" ,media, "Aprovado!")
elif media >= 4:
    print("Sua média é" ,media, "Está em recuperação!")
else:
    print("Sua média é" ,media, "Reprovado!")
