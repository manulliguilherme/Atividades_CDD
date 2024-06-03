#REVISÃO
#Faça um código que receba 4 números e realize a soma deles e a média entre eles, e mostre os resultados.
soma = 0
media = 0

for contador in range(0, 4, 1):
    numero = float(input('Digite os números: '))
    soma = soma + numero   ###########
media = soma / 4
print(f"A soma dos números é {soma}, e a média é {media}")
