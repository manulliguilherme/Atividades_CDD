#Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo recebido, caso
#o segundo valor digitado, seja zero, solicite novamente o valor, informando que só aceitaremos
# valor diferentes de zero.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

while valor2 == 0:
    valor2 = int(input('Valor inválido. Digite outro número: '))


divisao = valor1/ valor2
print(f"O valor da divisão é {divisao}")