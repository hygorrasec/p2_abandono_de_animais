from modules.pilha import Pilha
from modules.animal import Animal

class CadastrarAnimal:
    """
    Classe para Cadastrar Animal.
    
    animais             - pilha de animais
    cadastrar_animal()  - função para cadastrar animal
    pesquisar_animais() - função para pesquisar animais (retorna uma pilha de animais encontrados)
    """
    def __init__(self):
        self.animais = Pilha()

    def cadastrar_animal(self, especie, idade, cor, porte, particularidade):
        if especie == '' or idade == '' or cor == '' or porte == '':
            return
        if particularidade == '':
            particularidade = 'Não informado'
        animal = Animal(especie, idade, cor, porte, particularidade)
        self.animais.empilhar(animal)

    def pesquisar_animais(self, especie=None, idade=None, cor=None, porte=None, particularidade=None):
        animais_encontrados = Pilha()
        pilha_temp = Pilha()

        while not self.animais.vazia():  # enquanto a pilha não estiver vazia
            animal = self.animais.desempilhar()

            if (especie is None or animal.especie == especie) and \
               (idade is None or animal.idade == idade) and \
               (cor is None or animal.cor == cor) and \
               (porte is None or animal.porte == porte) and \
               (particularidade is None or animal.particularidade == particularidade):
                animais_encontrados.empilhar(animal)

            pilha_temp.empilhar(animal)

        while not pilha_temp.vazia():
            self.animais.empilhar(pilha_temp.desempilhar())

        return animais_encontrados
