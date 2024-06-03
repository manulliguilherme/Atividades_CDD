#Ler uma variável de número inteiro e mostrar a tabuada de multiplicação desse número

num = int(input('Digite apenas um número: '))
tabuada = 0

for a in range(1, 11):
    tabuada = num * a
   # print(f"{num} x {a} = {tabuada}")
    print("{} x {} = {}".format(num, a, tabuada))





