#Ler 10 valores, calcular e escrever a média aritmétrica
#com o professor

x = 0
soma = 0
while x < 10:
    n = float(input('Digite um número: '))
    soma = soma + n
    x = x + 1  #contador, no for já está dentro.
print (f"Valor final de X: {x}")

media = soma / 10
print(media)
