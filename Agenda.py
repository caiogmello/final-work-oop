from datetime import datetime, timedelta
# 3
class Agenda:
    def __init__(self):
        self._diasAlugados = []
        self._diasBloqueados = []

    # coloco todas as datas alugadas em uma lista de datas alugadas
    def alugarImovel(self, diaInicial, mesInicial, AnoInicial
                     , diaFinal, mesFinal, anoFinal):
        timeDelta = timedelta(days=1)
        dataInicial = datetime(int(AnoInicial), int(mesInicial), int(diaInicial))
        dataFinal = datetime(int(anoFinal), int(mesFinal), int(diaFinal))
        while dataInicial <= dataFinal:
            self._diasAlugados.append(dataInicial)
            dataInicial += timeDelta

    # coloco todas as datas bloqueadas em uma lista de datas bloqueadas
    def bloquearImovel(self, diaInicial, mesInicial, AnoInicial
                     , diaFinal, mesFinal, anoFinal):
        timeDelta = timedelta(days=1)
        dataInicial = datetime(int(AnoInicial), int(mesInicial), int(diaInicial))
        dataFinal = datetime(int(anoFinal), int(mesFinal), int(diaFinal))
        while dataInicial <= dataFinal:
            self._diasBloqueados.append(dataInicial)
            dataInicial += timeDelta
        
        def getDiasAlugados(self):
            return self._diasAlugados
        
        def getDiasBloqueados(self):
            return self._diasBloqueados
        
        def __str__(self):
            return f"{self._diasAlugados}, {self._diasBloqueados}"
        
