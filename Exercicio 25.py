#Ler 10 notas, calcular e escrever a média aritmétrica desses valores lidos

soma = 0
contador = 0

for k in range(10):
    valor = float(input('Digite o valor: '))
    if valor >= 0 and valor <= 10:
        soma = soma + valor
        contador = contador + 1
        print(f" A soma é {soma}, a média é {media}")

if contador != 0:
    media = soma / contador
else:
    print('ERRO!')
