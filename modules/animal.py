class Animal:
    """
    Classe para coletar dados do animal.
    """
    def __init__(self, tipo, idade, cor, porte, particularidade='Não informado'):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade
