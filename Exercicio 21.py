#Definir se o número é positivo ou negativo
negativo = 0
positivo = 0

for contador in range(10):
    valor = int(input("Digite um número: "))
    if valor < 0:
        negativo = negativo + 1
    else:
        positivo = positivo + 1

print(positivo)
print(negativo)


