from modules.animal import Animal  # tipo, idade, cor, porte, particularidade
from modules.pessoa import Pessoa  # nome, telefone, email, especie_interesse, preferencia_animal

# Criando uma instância da classe Animal e Pessoa
meu_animal = Animal('cachorro', 2, 'preto', 'grande')
pessoa_01 = Pessoa('João', '99999-9999', 'email@gmail.com', 'cachorro', 'grande')

# Acessando as informações do animal
print("Tipo:", meu_animal.tipo)
print("Idade:", meu_animal.idade)
print("Cor:", meu_animal.cor)
print("Porte:", meu_animal.porte)
print("Particularidade:", meu_animal.particularidade)

# Acessando as informações da pessoa
print("Nome:", pessoa_01.nome)
print("Telefone:", pessoa_01.telefone)
print("Email:", pessoa_01.email)
print("Especie de interesse:", pessoa_01.especie_interesse)
print("Preferencia de animal:", pessoa_01.preferencia_animal)
