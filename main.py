# Autores: Fabio Lima e Hygor Rasec
# Curso: Engenharia de Software
# Disciplina: Estrutura de Dados
# Professor: Marcio Garrido
# Data: 15/06/2023

'''
A prefeitura necessita de um sistema capaz de cadastrar todos os animais de acordo com seu tipo (canino, felino, etc.), sendo fundamental a capacidade de inserir novos tipos de animais de forma dinâmica. Além disso, é necessário classificá-los de acordo com a idade aproximada, cor, porte e qualquer particularidade que possuam. No mesmo sistema, deve haver um cadastro das pessoas interessadas em adoção, contendo as informações de contato e a espécie pela qual estão interessadas. Ao selecionar a espécie desejada, o sistema também deve permitir que sejam especificadas preferências em relação ao animal.

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


def menu():
    animais = CadastrarAnimal()
    while True:
        pesquisar_animal = animais.pesquisar_animais()
        print('Menu: ')
        print('1 - Cadastrar Animal')
        print('2 - Pesquisar Animais Disponíveis')
        print('3 - Sair')
        opcao = input('> ')

        if opcao == '1':

            while True:
                tipo_animal = input('\nInforme o tipo de Animal (ex: canino, felino): ')
                idade = input('Informe a idade em anos: ')
                cor = input('Informe a cor: ')
                porte = input('Informe o porte (pequeno, médio ou grande): ')
                particularidade = input('Informe alguma particularidade (se não tiver pode deixar em branco): ')
                
                animais.cadastrar_animal(tipo_animal, idade, cor, porte, particularidade)

                continuar = input('\nContinuar cadastrando animais (digite "s" para continuar ou "n" para sair): ')
                
                if continuar == 'n':
                    print()
                    break

        elif opcao == '2':

            if pesquisar_animal.vazia():
                print('\nNão tem animais disponíveis.\n')
            else:
                print('\nAnimais disponíveis:\n')
                while not pesquisar_animal.vazia():
                    animal = pesquisar_animal.desempilhar()
                    print(f'Tipo: {animal.tipo}, Idade: {animal.idade}, Cor: {animal.cor}, Porte: {animal.porte}, Particularidade: {animal.particularidade}')
                print()

        elif opcao == '3':
            print('\nSaindo do programa... ')
            break
        else:
            print('Opção inválida!')


def main():
    menu()


if __name__ == '__main__':  # condição que verifica se o módulo está sendo executado diretamente (ou seja, não sendo importado por outro módulo).
    main()