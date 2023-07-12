class Endereco:
    def __init__(self, rua, numero, cidade, estado, cep):
        self._rua = rua
        self._numero = numero
        self._cidade = cidade
        self._estado = estado
        self._cep = cep

    def getRua(self):
        return self._rua

    def getNumero(self):
        return self._numero
    
    def getCidade(self):
        return self._cidade
    
    def getEstado(self):
        return self._estado
    
    def getCep(self):
        return self._cep
    
    def setRua(self, rua):
        self._rua = rua

    def setNumero(self, numero):
        self._numero = numero

    def setCidade(self, cidade):
        self._cidade = cidade

    def setEstado(self, estado):
        self._estado = estado

    def setCep(self, cep):
        self._cep = cep

    def __str__(self):
        return f"{self._rua}, {self._numero}, {self._cidade}, {self._estado}, {self._cep}"
    