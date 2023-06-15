class Pessoa:
    """
    Classe para coletar dados da pessoa.
    """
    def __init__(self, nome, telefone, email, especie_interesse, preferencia_animal='Não informado'):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.especie_interesse = especie_interesse
        self.preferencia_animal = preferencia_animal
