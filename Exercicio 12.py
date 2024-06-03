#Receba um número do usuário e diga se ele é par ou ímpar

numero = int(input("Digite um número:"))

if numero == 0:
    print('O número é igual a 0')
elif numero % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")