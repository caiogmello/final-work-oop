class Endereco:
    def __init__(self, rua, numero, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def getRua(self):
        return self.rua

    def getNumero(self):
        return self.numero
    
    def getCidade(self):
        return self.cidade
    
    def getEstado(self):
        return self.estado
    
    def getCep(self):
        return self.cep
    
    def setRua(self, rua):
        self.rua = rua

    def setNumero(self, numero):
        self.numero = numero

    def setCidade(self, cidade):
        self.cidade = cidade

    def setEstado(self, estado):
        self.estado = estado

    def setCep(self, cep):
        self.cep = cep

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cidade}, {self.estado}, {self.cep}"
    