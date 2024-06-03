#Faça um código para ler a senha de um usuário e após 3 tentativas erradas, sair do prograa, informando
#que a senha está bloqueada

senha = 1234
contador = 0

login = int(input('Digite a sua senha: '))
contador = contador + 1

while login != senha:
   login = int(input('Senha incorreta! Digite novamente: '))
   contador = contador + 1
   if contador == 3 and login != senha:
       print('Senha bloqueada')
       break
else:
    print('Senha correta')


print('Fim de programa')













