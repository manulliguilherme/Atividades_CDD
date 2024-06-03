#Ler um vetor A de 10 núemros. Logo em seguida, ler mais um número e guardar em uma variavel X.
#Armazenar em um vetor M, o resultado de cada elemento de A multiplicação pelo valor X. Logo após,
#imprimir o vetor M

x = 0
a = [0,0,0,0,0,0,0,0,0,0]
m = [0,0,0,0,0,0,0,0,0,0]

for contador in range(0, len(a), 1):
    a[contador] = int(input('Digite o número: '))

x = int(input('Digite o número para multiplicar: '))

for contador1 in range(0, len(a), 1):
    m[contador1] = x * a[contador1]

print(a)
print(x)
print(m)


