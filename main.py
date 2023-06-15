# Autores: Fabio Lima e Hygor Rasec
# Curso: Engenharia de Software
# Disciplina: Estrutura de Dados
# Professor: Marcio Garrido
# Data: 15/06/2023

'''
A prefeitura necessita de um sistema capaz de cadastrar todos os animais de acordo com sua especie (canino, felino, etc.), sendo fundamental a capacidade de inserir novas espécies de animais de forma dinâmica. Além disso, é necessário classificá-los de acordo com a idade aproximada, cor, porte e qualquer particularidade que possuam. No mesmo sistema, deve haver um cadastro das pessoas interessadas em adoção, contendo as informações de contato e a espécie pela qual estão interessadas. Ao selecionar a espécie desejada, o sistema também deve permitir que sejam especificadas preferências em relação ao animal.

Por fim, no final de cada mês, a prefeitura emitirá um relatório que cruza as espécies disponíveis com os possíveis candidatos à adoção. Além disso, sempre que um candidato entrar em contato para adotar, o atendente poderá pesquisar se há algum animal com as características informadas.

Os alunos registraram atentamente todas as observações, elaboraram o fluxograma do estudo de caso e, posteriormente, desenvolveram o primeiro protótipo em Python, mesmo que em formato de texto e sem requisitos gráficos. A intenção foi apenas validar a proposta do programa junto ao solicitante.

Exemplo usado: Pilhas (LIFO - Last In, First Out)
Uma pilha é uma estrutura de dados que segue o princípio LIFO (Last In, First Out), o que significa que o último elemento inserido é o primeiro a ser removido. Em uma pilha, as operações de inserção e remoção são realizadas em uma extremidade chamada topo.

Resumindo, uma pilha é uma coleção de elementos organizados em que as operações de inserção (empilhar) e remoção (desempilhar) ocorrem somente em uma extremidade da estrutura, o topo da pilha.

Aqui está um exemplo de representação visual de uma pilha:

    +---+
    | 5 | <- Topo da pilha (primeiro a ser removido)
    +---+
    | 3 |
    +---+
    | 2 |
    +---+
    | 7 |
    +---+
    | 1 |
    +---+

'''


from modules.cadastrar_animal import CadastrarAnimal
from modules.cadastrar_pessoa import CadastrarPessoa
from modules.funcoes_validacao import *
from modules.functions import *


def menu():
    animais = CadastrarAnimal()
    pessoas = CadastrarPessoa()
    while True:
        pesquisar_animal = animais.pesquisar_animais()
        pesquisar_pessoas = pessoas.pesquisar_pessoas()
        print()
        print('\033[1;90m=\033[m'*35)
        cabecalho('\033[1;32m<<<SISTEMA DE ADOÇÃO>>>\033[m')
        print('\033[1;90m=\033[m'*35)
        cabecalho('''\033[1;91m
[1] Cadastrar Animal
[2] Cadastrar Pessoa
[3] Pesquisar Animais Disponíveis
[4] Pesquisar Pessoas Interessadas
[5] Gerar Relatório
[6] Sair
        \033[m''')
        opcao = verificar_opcao('\033[1;36mInforme uma opção: \033[m', '\033[1;31mDigite apenas números.\033[m')

        if opcao == 1:
            cadastrar_animal(animais)
        elif opcao == 2:
            cadastrar_pessoa(pessoas)
        elif opcao == 3:
            pesquisar_animais_disponiveis(pesquisar_animal)
        elif opcao == 4:
            pesquisar_pessoas_interessadas(pessoas)
        elif opcao == 5:
            gerar_relatorio(pesquisar_animal, pesquisar_pessoas)
        elif opcao == 6:
            print('\nSaindo do programa... ')
            break
        else:
            print('\nOpção inválida!\n')


def main():
    menu()


if __name__ == '__main__':  # condição que verifica se o módulo está sendo executado diretamente (ou seja, não sendo importado por outro módulo).
    main()
