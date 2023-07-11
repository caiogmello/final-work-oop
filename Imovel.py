from Endereco import Endereco
class Imovel:
    def __init__(self, iptu, rua, numero, cep, tipo, utilizacao, estado="Bahia", cidade="Salvador"):
        self.iptu = iptu
        self.endereco = Endereco(rua, numero, cidade, estado, cep)
        self.tipo = tipo
        self.utilizacao = utilizacao
