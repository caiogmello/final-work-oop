from datetime import datetime, timedelta

class Agenda:
    def __init__(self):
        self._diasAlugados = []
        self._diasBloqueados = []
    
    def alugarImovel(self, diaInicial, mesInicial, AnoInicial
                     , diaFinal, mesFinal, anoFinal):
        timeDelta = timedelta(days=1)
        dataInicial = datetime(int(AnoInicial), int(mesInicial), int(diaInicial))
        dataFinal = datetime(int(anoFinal), int(mesFinal), int(diaFinal))
        while dataInicial <= dataFinal:
            self._diasAlugados.append(dataInicial)
            dataInicial += timeDelta
        
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
        
