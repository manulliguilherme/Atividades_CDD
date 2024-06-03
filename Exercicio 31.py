#Refaça o exercicio anterior, agora implementando a pergunta "Deseja realizar um novo cálculo?"

novo = 'S'    #NÃO PRECISA ADICIONAR O S minúscúlo
while novo == 'S' or novo == 's':
    nota1 = float(input('Digite a primeira nota: '))
    while nota1 <0 or nota1 > 10:
        nota1 = float(input('Nota não aceita. Digite a primeira nota novamente: '))


    nota2 = float(input('Digite a segunda nota: '))
    while nota2 < 0 or nota2 >10:
        nota2 = float(input('Nota não aceita. Digite a segunda nota novamente: '))

    soma = nota1 + nota2
    media = soma / 2

    print(f"A média do aluno é {media}")

    novo = input('Você deseja realizar um novo cálculo ?')