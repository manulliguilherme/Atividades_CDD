#Receba dois numeros do usuário e mostre em ordem crescente


n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("Então",n2, "é menor que",n1)
else:
    print("Então",n1, "é menor que",n2)