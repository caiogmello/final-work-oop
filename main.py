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
        print("7 - Atualizar endereço de proprietário")
        print("8 - Sair \n")
        opcao = input("Digite a opção: ")
        if opcao == "1":
            print("\nCadastrando proprietário\n")
            simulator.cadastrarProprietario()
        elif opcao == "2":
            print("\nCadastrando imóvel\n")
            simulator.cadastrarImovel()
        elif opcao == "3":
            print("\nListando proprietários\n")
            simulator.listarProprietarios()
        elif opcao == "4":
            print("\nListando imóveis\n")
            simulator.listarImoveis()
        elif opcao == "5":
            print("\nBloqueando imóvel\n")
            simulator.bloquearImovel()
        elif opcao == "6":
            print("\nAlugando imóvel\n")
            simulator.alugarImovel()
        elif opcao == "7":
            print("\nAtualizando endereço de proprietário\n")
            simulator.atualizarEnderecoProprietario()
        elif opcao == "8":
            print("\nSaindo do sistema...\n")
            break

if __name__ == "__main__":
    run()



