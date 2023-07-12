from Endereco import Endereco
from Agenda import Agenda
# 1
class Imovel:
    # 1.a / 1.b
    def __init__(self, iptu, rua, numero, cep, tipo, utilizacao, estado="Bahia", cidade="Salvador"):
        self.iptu = iptu
        self.endereco = Endereco(rua, numero, cidade, estado, cep)
        self.tipo = tipo.lower()
        self.utilizacao = utilizacao
        self._agenda = Agenda()

    def alugar(self, diaInicial, mesInicial, AnoInicial
                     , diaFinal, mesFinal, anoFinal):
        self._agenda.alugarImovel(diaInicial, mesInicial, AnoInicial
                                    , diaFinal, mesFinal, anoFinal)
    
    def bloquear(self, diaInicial, mesInicial, AnoInicial
                        , diaFinal, mesFinal, anoFinal):
        self._agenda.bloquearImovel(diaInicial, mesInicial, AnoInicial
                                    , diaFinal, mesFinal, anoFinal)

    def getIptu(self):
        return self.iptu
    
    def getEndereco(self):
        return self.endereco
    
    def getTipo(self):
        return self.tipo
    
    def getUtilizacao(self):
        return self.utilizacao
    
    def getDiasAlugados(self):
        return self._agenda.getDiasAlugados()
    
    def getDiasBloqueados(self):
        return self._agenda.getDiasBloqueados()
    
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