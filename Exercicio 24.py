#Ler 10 valores, calcular e escrever a média aritmétrica desses valores lidos

soma = 0
media = 0

for contador in range(10):
    valor = int(input('Digite o valor: '))
    soma = soma + valor

media = soma / 10

print(f"O valor da soma é:  {soma}, e o valor da média é: {media} ")



