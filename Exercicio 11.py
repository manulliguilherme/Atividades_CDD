#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado do
#da seguinte forma: E- Etanol, G-Gasolina), calcule e imprima o valor a ser pago pelo cliente
#sabendo-se que o preço do litro da gasolina é R$:5.80 e o preço do litro do etal é R$:4.90



tipo = input("Escolha o tipo de combustível (G - Gasolina ou E-Etanol): ")
litros = float(input("Quantos litros de combustível você deseja?"))

G = 5.80
E = 4.90

if tipo == "G" or tipo == "g":
    pfinal = G * litros
    print(pfinal)
elif tipo == "E" or tipo == "e":
    pfinal = E * litros
    print(pfinal)
else:
    print('Erro! Tipo de combustivel não encontrado. ')
