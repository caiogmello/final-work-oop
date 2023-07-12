from Endereco import Endereco

# 1
class Proprietario:
    # 1.b
    def __init__(self, nome, cpf, identidade,rua, numero, cidade, estado, cep):
        self._nome = nome
        self._cpf = cpf
        self._identidade = identidade
        self._endereco = Endereco(rua, numero, cidade, estado, cep)
        self._imoveis = []

    def adicionarImovel(self, imovel):
        # 2
        if imovel.getEndereco() == self._endereco:
            print("Esse imóvel é do próprio proprietário. \n")
            return False
        self._imoveis.append(imovel)
        return True

    # 2.a
    def listarImoveis(self, tipo):
        print("\n=== Imoveis de " + self.getNome() + "do tipo " + tipo + " ===\n")
        for imovel in self._imoveis:
            if imovel.getTipo() == tipo.lower():
                print("  - ", end="")
                print(imovel)
    # 1.d
    # Criei apenas um método pois não existe o conceito de overload em Python
    def atualizarEndereco(self, rua, numero, cep, estado, cidade):
        self._endereco.setRua(rua)
        self._endereco.setNumero(numero)
        self._endereco.setCep(cep)
        if estado != "":
            self._endereco.setEstado(estado)
        if cidade != "":
            self._endereco.setCidade(cidade)


    def getImoveis(self):
        return self._imoveis

    def getNome(self):
        return self._nome
    
    def getCpf(self):
        return self._cpf
    
    def getIdentidade(self):
        return self._identidade
    
    def getEndereco(self):
        return self._endereco
    
    def setNome(self, nome):
        self._nome = nome

    def setCpf(self, cpf):
        self._cpf = cpf

    def setIdentidade(self, identidade):
        self._identidade = identidade
        
    def __str__(self):
        return f"{self._nome}, {self._cpf}, {self._endereco}"
    