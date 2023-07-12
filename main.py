from Simulator import Simulator

def run():
    simulator = Simulator()
    print("\nBem vindo ao sistema de aluguel de imóveis! \n")

    while True:
        print("Digite o número correspondente a opção desejada: \n")
        print("1 - Cadastrar proprietário")
        print("2 - Cadastrar imóvel")
        print("3 - Listar proprietários")
        print("4 - Listar imóveis")
        print("5 - Bloquear imóvel")
        print("6 - Alugar imóvel")
        print("7 - Sair \n")
        opcao = input("Digite a opção: ")
        if opcao == "1":
            print("\nCadastrando proprietário\n")
            simulator.cadastrarProprietario()
        elif opcao == "2":
            print("\nCadastrando imóvel\n")
            simulator.cadastrarImovel()
        elif opcao == "3":
            simulator.listarProprietarios()
        elif opcao == "4":
            simulator.listarImoveis()
        elif opcao == "5":
            simulator.bloquearImovel()
        elif opcao == "6":
            simulator.alugarImovel()
        elif opcao == "7":
            print("\nSaindo do sistema...\n")
            break

run()



