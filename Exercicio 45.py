#

opcao = -1
une = 0
while opcao != 3:
   une = 0
   opcao = int(input("Escolha sua opção : 1 - para cadastro de usuário 2 - para fazer o login 3- para sair:  "))
   if opcao == 1:
       nomes = ['', '', '', '', '']
       senhas = ['', '', '', '', '']
       for x in range(5):
           nomes[x] = input('Digite o nome:')
           senhas[x] = input(f'Digite as senhas:')
       for z in range(5):
           print(z,nomes[z], senhas[z])

   elif opcao == 2:
       login = input('Digite o nome do usuário: ')
       senha = input('Digite a senha: ')
       for y in range(5):
           if login == nomes[y]:
               if senha == senhas[y]:
                   print('Login efetuado com sucesso')
               else:
                   print('Senha inválida')
           else:
               une = une + 1
   if une == 5:
        print ('Usuário não existe!')

else:
   print('Até logo')