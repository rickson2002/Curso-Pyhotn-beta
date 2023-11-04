# if  /     elif        / else
# se /  se não se          / senão

nome = str(input("Digite seu nome: "))

entrada = input(f'Ola {nome}, voce deseja "Entrar" ou " Sair" ? ')

if entrada == "entrar":

    print("Voce entrou no sistema, seja Bem vindo!!")

elif entrada == "sair":

    print("Voce saiu do sistema, até a proxima")

else:

    print("Opa, voce não digitou nenhuma das outras opçoes anteriores, digite de novo!")