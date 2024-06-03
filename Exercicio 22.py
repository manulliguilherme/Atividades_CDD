#Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20]
# (incluindo 10 e 20 no intervalo) e quantos deles estão fora e dentro deste intervalo

numeros = 0
fora = 0

for contador in range(11, 21, 1):
    valor = int(input('Digite um número: '))
    if valor >= 10 and valor <= 20:
        numeros = numeros + 1
    else:
        fora = fora + 1

print(f"{numeros} estão dentro do intervalo, e {fora} estão fora do intervalo")

