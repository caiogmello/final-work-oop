from Endereco import Endereco
class Proprietario:
    def __init__(self, nome, cpf, rua, numero, cidade, estado, cep):
        self._nome = nome
        self._cpf = cpf
        self._endereco = Endereco(rua, numero, cidade, estado, cep)

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

    def atualizarEndereco(self, rua, numero, cep, estado, cidade):
        self.endereco.setRua(rua)
        self.endereco.setNumero(numero)
        self.endereco.setCep(cep)
        if estado != None:
            self.endereco.setEstado(estado)
        if cidade != None:
            self.endereco.setCidade(cidade)


        

    def __str__(self):
        return f"{self._nome}, {self._cpf}, {self._endereco}"
    