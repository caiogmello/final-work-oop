from Endereco import Endereco
# 1
class Proprietario:
    # 1.b
    def __init__(self, nome, cpf, rua, numero, cidade, estado, cep):
        self._nome = nome
        self._cpf = cpf
        self._endereco = Endereco(rua, numero, cidade, estado, cep)
        self._imoveis = []

    def adicionarImovel(self, imovel):
        self._imoveis.append(imovel)
        
    # 2.a
    def listarImoveis(self, tipo):
        for imovel in self._imoveis:
            if imovel.getTipo() == tipo:
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


    def getNome(self):
        return self.nome
    
    def getCpf(self):
        return self.cpf
    
    def getEndereco(self):
        return self.endereco
    
    def setNome(self, nome):
        self.nome = nome

    def setCpf(self, cpf):
        self.cpf = cpf
        
    def __str__(self):
        return f"{self._nome}, {self._cpf}, {self._endereco}"
    