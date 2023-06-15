from modules.pilha import Pilha
from modules.pessoa import Pessoa

class CadastrarPessoa:
    """
    Classe para Cadastrar Pessoa.
    
    pessoas             - pilha de pessoas
    cadastrar_pessoa()  - função para cadastrar pessoa
    pesquisar_pessoas() - função para pesquisar pessoas (retorna uma pilha de pessoas encontrados)
    """
    def __init__(self):
        self.pessoas = Pilha()

    def cadastrar_pessoa(self, nome, telefone, email, especie_interesse, preferencia_animal):
        pessoa = Pessoa(nome, telefone, email, especie_interesse, preferencia_animal)
        self.pessoas.empilhar(pessoa)

    def pesquisar_pessoas(self, especie_interesse=None, preferencia_animal=None):
        pessoas_encontradas = Pilha()
        pilha_temp = Pilha()

        def pesquisa_recursiva():
            if self.pessoas.vazia():
               return

            pessoa = self.pessoas.desempilhar()

            if (especie_interesse is None or pessoa.especie_interesse == especie_interesse) and \
               (preferencia_animal is None or pessoa.preferencia_animal == preferencia_animal):
                pessoas_encontradas.empilhar(pessoa)

            pilha_temp.empilhar(pessoa)
            pesquisa_recursiva()


        pesquisa_recursiva()

        while not pilha_temp.vazia():
            self.pessoas.empilhar(pilha_temp.desempilhar())

        return pessoas_encontradas
