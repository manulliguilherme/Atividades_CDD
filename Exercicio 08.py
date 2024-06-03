##Receba dois numeros do usuário e mostre em ordem crescente e se são iguais

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número: "))

if n1 == n2:
    print("Números iguais")
else:
    if n1 < n2:
        print(n1, n2)
    else:
        print(n2, n1)