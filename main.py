from Imovel import Imovel
from Proprietario import Proprietario

Imovel = Imovel(123, "Rua 1", 123, 123, "Casa", "Residencial")
print(Imovel)
Proprietario = Proprietario("Joao", 123, "Rua 1", 123, "Salvador", "Bahia", 123)
print(Proprietario)
Proprietario.atualizarEndereco("Rua 2", 456, 45226, "","")
print(Proprietario)

