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
from modules.cadastrar_pessoa import CadastrarPessoa
from modules.funcoes_validaçao import *

def gerar_relatorio(animais, pessoas):
    print("Relatório de Cruzamento de Espécies Disponíveis x Possíveis Candidatos:")
    
    while not animais.vazia() and not pessoas.vazia():
        animal = animais.desempilhar()
        pessoa = pessoas.desempilhar()

        if animal.tipo == pessoa.especie_interesse:
            print(f"Animal: Tipo: {animal.tipo}, Idade: {animal.idade}, Cor: {animal.cor}, Porte: {animal.porte}, Particularidade: {animal.particularidade}")
            print(f"Candidato: Nome: {pessoa.nome}, Contato: {pessoa.contato}, Espécie de interesse: {pessoa.especie_interesse}, Preferência: {pessoa.preferencia}\n")

    if animais.vazia() or pessoas.vazia():
        print("Não há cruzamento de espécies disponíveis x possíveis candidatos.")


def menu():
    animais = CadastrarAnimal()
    pessoas = CadastrarPessoa()
    while True:
        pesquisar_animal = animais.pesquisar_animais()
        cabecalho('\033[1;32m<<<SISTEMA DE ADOÇÃO>>>\033[m')
        cabecalho('''\033[1;91m
[1] Cadastrar Animal
[2] Cadastrar Pessoa
[3] Pesquisar Animais Disponíveis
[4] Pesquisar Pessoas Interessadas
[5] Sair
          \033[m''')
        opcao = verificar_opcao('\033[1;36mInforme uma opção: \033[m', '\033[1;31mDigite apenas números.\033[m')

        if opcao == 1:

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

        elif opcao == 2:

            nome = input("\nInforme o nome: ")
            telefone = input("Informe o telefone: ")
            email = input("Informe o email: ")
            especie_interesse = input("Informe a espécie de interesse (ex: canino, felino): ")
            preferencia_animal = input("Informe a preferência do animal: ")
            pessoas.cadastrar_pessoa(nome, telefone, email, especie_interesse, preferencia_animal)
            print("\nPessoa cadastrada com sucesso!\n")

        elif opcao == 3:

            if pesquisar_animal.vazia():
                print('\nNão tem animais disponíveis.\n')
            else:
                print('\nAnimais disponíveis:\n')
                while not pesquisar_animal.vazia():
                    animal = pesquisar_animal.desempilhar()
                    print(f'Tipo: {animal.tipo}, Idade: {animal.idade}, Cor: {animal.cor}, Porte: {animal.porte}, Particularidade: {animal.particularidade}')
                print()

        elif opcao == 4:
            
            especie_interesse = input("\nNome da especie que a pessoa tenha interesse (ex: canino, felino): ")
            preferencia_animal = input("Informe a preferência do animal: (ex: adulto) ")
            pessoas_encontradas = pessoas.pesquisar_pessoas(especie_interesse, preferencia_animal)
            if pessoas_encontradas.vazia():
                print("\nNão tem pessoas interessadas.\n")
            else:
                print("\nPessoas interessadas:\n")
                while not pessoas_encontradas.vazia():
                    pessoa = pessoas_encontradas.desempilhar()
                    print(f"Nome: {pessoa.nome}, Telefone: {pessoa.telefone}, Espécie de interesse: {pessoa.especie_interesse}, Preferência: {pessoa.preferencia_animal}")
                print()

        elif opcao == 5:
            print('\nSaindo do programa... ')
            break
        else:
            print('\nOpção inválida!\n')


def main():
    menu()


if __name__ == '__main__':  # condição que verifica se o módulo está sendo executado diretamente (ou seja, não sendo importado por outro módulo).
    main()
