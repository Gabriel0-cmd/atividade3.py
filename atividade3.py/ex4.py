opcao = 0

while opcao != 3:
    print("1 - Olá")
    print("2 - Ajuda")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá!")
    if opcao == 2:
        print("Ajuda aqui.")
    if opcao == 3:
        print("Tchau!")