from Endereco import Endereco
# 1
class Imovel:
    # 1.a / 1.b
    def __init__(self, iptu, rua, numero, cep, tipo, utilizacao, estado="Bahia", cidade="Salvador"):
        self.iptu = iptu
        self.endereco = Endereco(rua, numero, cidade, estado, cep)
        self.tipo = tipo
        self.utilizacao = utilizacao

    def getIptu(self):
        return self.iptu
    
    def getEndereco(self):
        return self.endereco
    
    def getTipo(self):
        return self.tipo
    
    def getUtilizacao(self):
        return self.utilizacao
    
    def setIptu(self, iptu):
        self.iptu = iptu

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setTipo(self, tipo):
        self.tipo = tipo

    def setUtilizacao(self, utilizacao):
        self.utilizacao = utilizacao

    def __str__(self):
        return f"{self.iptu}, {self.endereco}, {self.tipo}, {self.utilizacao}"