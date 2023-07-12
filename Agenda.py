from datetime import datetime, timedelta

class Agenda:
    def __init__(self):
        self._diasAlugados = []
        self._diasBloqueados = []
    
    def alugarImovel(self, diaInicial, mesInicial, AnoInicial
                     , diaFinal="", mesFinal="", anoFinal=""):
        timeDelta = timedelta(days=1)
        dataInicial = datetime(AnoInicial, mesInicial, diaInicial)
        if diaFinal == "":
            diaFinal = diaInicial
        if mesFinal == "":
            mesFinal = mesInicial
        if anoFinal == "":
            anoFinal = AnoInicial
        dataFinal = datetime(anoFinal, mesFinal, diaFinal)
        while dataInicial <= dataFinal:
            self._diasAlugados.append(dataInicial)
            dataInicial += timeDelta
        
    def bloquearImovel(self, diaInicial, mesInicial, AnoInicial
                     , diaFinal="", mesFinal="", anoFinal=""):
        timeDelta = timedelta(days=1)
        dataInicial = datetime(AnoInicial, mesInicial, diaInicial)
        if diaFinal == "":
            diaFinal = diaInicial
        if mesFinal == "":
            mesFinal = mesInicial
        if anoFinal == "":
            anoFinal = AnoInicial
        dataFinal = datetime(anoFinal, mesFinal, diaFinal)
        while dataInicial <= dataFinal:
            self._diasBloqueados.append(dataInicial)
            dataInicial += timeDelta
        
        def getDiasAlugados(self):
            return self._diasAlugados
        
        def getDiasBloqueados(self):
            return self._diasBloqueados
        
        def __str__(self):
            return f"{self._diasAlugados}, {self._diasBloqueados}"
        
        