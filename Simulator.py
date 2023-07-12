from Imovel import Imovel
from Proprietario import Proprietario


class Simulator:
    def __init__(self):
        self._proprietarios = []

    def cadastrarProprietario(self):
        nome = input("Digite o nome do proprietario: ")
        cpf = input("Digite o cpf do proprietario: ")
        # if self.buscaProprietario(cpf) != None:
        #     print("Proprietario ja cadastrado \n")
        #     return False
        identidade = input("Digite a identidade do proprietario: ")
        rua = input("Digite a rua do proprietario: ")
        numero = input("Digite o numero do proprietario: ")
        cidade = input("Digite a cidade do proprietario: ")
        estado = input("Digite o estado do proprietario: ")
        cep = input("Digite o cep do proprietario: ")
        print("Proprietario cadastrado com sucesso \n")
        proprietario = Proprietario(nome, cpf, identidade, rua, numero, cidade, estado, cep)
        # print(len(self._proprietarios))
        self._proprietarios.append(proprietario)
        # print(len(self._proprietarios))
        return True
    
                
    def listarProprietarios(self):
        print("\n Proprietarios: \n")
        # print(len(self._proprietarios))
        for proprietario in self._proprietarios:
            print("  - " + proprietario.getNome())
        print("\n")
    
    def cadastrarImovel(self):
        iptu = input("Digite o iptu do imovel: ")
        rua = input("Digite a rua do imovel: ")
        numero = input("Digite o numero do imovel: ")
        cidade = input("Digite a cidade do imovel: ")
        estado = input("Digite o estado do imovel: ")
        cep = input("Digite o cep do imovel: ")
        tipo = input("Digite o tipo do imovel: ")
        utilizacao = input("Digite a utilizacao do imovel: ")
        imovel = Imovel(iptu, rua, numero, cep, tipo, utilizacao, estado, cidade)
        print("Deseja cadastrar o proprietario do imovel? \n")
        print("1 - Sim")
        print("2 - Nao \n")
        opcao = input("Digite a opcao: ")
        if opcao == "1":
            cpf = input("\nDigite o cpf do proprietario: ")
            proprietario = self.buscaProprietario(cpf)
            if proprietario == None:
                print("Proprietario não encontrado. \n")
                return False
            else:
                proprietario.adicionarImovel(imovel)
                print("\nImovel adicionado ao proprietário " + proprietario.getNome() + ".\n")
                return True


    def listarImoveis(self):
        proprietario = self.buscaProprietario(input("Digite o cpf do proprietario: "))
        if proprietario == None:
            print("\n Proprietario não encontrado. \n")
            return False
        else:
            tipo = input("Digite o tipo do imovel (CASA/APTO): ")
            proprietario.listarImoveis(tipo)
    def bloquearImovel(self):
        proprietario = self.buscaProprietario(input("Digite o cpf do proprietario: "))
        if proprietario == None:
            print("\n Proprietario não encontrado. \n")
            return False
        else:
            iptu = input("Digite o iptu do imovel: ")
            imovel = self.buscaImovel(iptu, proprietario.getImoveis())
            if imovel == None:
                print("\n Imovel não encontrado. \n")
                return False
            else:
                n = input("Deseja bloquear para mais de um dia? (S/N) ")
                diaInicial = input("Digite o dia inicial: ")
                mesInicial = input("Digite o mes inicial: ")
                anoInicial = input("Digite o ano inicial: ")
                if n.upper() == "S":
                    diaFinal = input("Digite o dia final: ")
                    mesFinal = input("Digite o mes final: ")
                    anoFinal = input("Digite o ano final: ")
                    imovel.bloquear(diaInicial, mesInicial, anoInicial, diaFinal, mesFinal, anoFinal)
                else:
                    imovel.bloquear(diaInicial, mesInicial, anoInicial,diaInicial, mesInicial, anoInicial)
            
                print("\n Imovel bloqueado com sucesso. \n")
                return True
    
    def alugarImovel(self):
        proprietario = self.buscaProprietario(input("Digite o cpf do proprietario: "))
        if proprietario == None:
            print("\n Proprietario não encontrado. \n")
            return False
        else:
            iptu = input("Digite o iptu do imovel: ")
            imovel = self.buscaImovel(iptu, proprietario.getImoveis())
            if imovel == None:
                print("\n Imovel não encontrado. \n")
                return False
            else:
                n = input("Deseja alugar para mais de um dia? (S/N) ")
                diaInicial = input("Digite o dia inicial: ")
                mesInicial = input("Digite o mes inicial: ")
                anoInicial = input("Digite o ano inicial: ")
                if n == "S":
                    diaFinal = input("Digite o dia final: ")
                    mesFinal = input("Digite o mes final: ")
                    anoFinal = input("Digite o ano final: ")
                    imovel.bloquear(diaInicial, mesInicial, anoInicial, diaFinal, mesFinal, anoFinal)
                else:
                    imovel.bloquear(diaInicial, mesInicial, anoInicial, diaInicial, mesInicial, anoInicial)
            
                print("\n Imovel alugado com sucesso. \n")
                return True

    def buscaImovel(self, iptu, imoveis):
        for imovel in imoveis:
            if imovel.getIptu() == iptu:
                return imovel
        return None

    def buscaProprietario(self, cpf):
        for proprietario in self._proprietarios:
            if proprietario.getCpf() == cpf:
                return proprietario
        return None
