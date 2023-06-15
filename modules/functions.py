def cadastrar_animal(animais):
    while True:
        especie_animal = input('\nInforme a espécie de animal (ex: canino, felino): ')
        idade = input('Informe a idade (em anos): ')
        cor = input('Informe a cor: ')
        porte = input('Informe o porte (pequeno, médio ou grande): ')
        particularidade = input('Informe alguma particularidade: (ex: adulto) ')
        
        animais.cadastrar_animal(especie_animal, idade, cor, porte, particularidade)

        continuar = input('\nContinuar cadastrando animais (digite "s" para continuar ou "n" para sair): ')
        
        if continuar == 'n':
            print()
            break


def cadastrar_pessoa(pessoas):
    nome = input('\nInforme o nome: ')
    telefone = input('Informe o telefone: ')
    email = input('Informe o email: ')
    especie_interesse = input('Informe a espécie de interesse (ex: canino, felino): ')
    preferencia_animal = input('Informe a preferência do animal de interesse: (ex: adulto) ')
    pessoas.cadastrar_pessoa(nome, telefone, email, especie_interesse, preferencia_animal)
    print('\nPessoa cadastrada com sucesso!')


def pesquisar_animais_disponiveis(pesquisar_animal):
    if pesquisar_animal.vazia():
        print('\nNão tem animais disponíveis.')
    else:
        print('\nAnimais disponíveis:\n')
        while not pesquisar_animal.vazia():
            animal = pesquisar_animal.desempilhar()
            print(f'Espécie: {animal.especie}, Idade: {animal.idade}, Cor: {animal.cor}, Porte: {animal.porte}, Particularidade: {animal.particularidade}')


def pesquisar_pessoas_interessadas(pessoas):
    especie_interesse = input('\nNome da espécie que a pessoa tenha interesse (ex: canino, felino): ')
    preferencia_animal = input('Informe a preferência do animal de interesse: (ex: adulto) ')
    pessoas_encontradas = pessoas.pesquisar_pessoas(especie_interesse, preferencia_animal)
    if pessoas_encontradas.vazia():
        print('\nNão tem pessoas interessadas.')
    else:
        print('\nPessoas interessadas:\n')
        while not pessoas_encontradas.vazia():
            pessoa = pessoas_encontradas.desempilhar()
            print(f'Nome: {pessoa.nome}, Telefone: {pessoa.telefone}, Espécie de interesse: {pessoa.especie_interesse}, Preferência: {pessoa.preferencia_animal}')
            

def gerar_relatorio(pesquisar_animal, pesquisar_pessoas):
    print('\nRelatório de Cruzamento de Espécies Disponíveis x Possíveis Candidatos:\n')

    if pesquisar_animal.vazia() or pesquisar_pessoas.vazia():
        print('Não há cruzamento de Espécies Disponíveis x Possíveis Candidatos.')
    else:
        while not pesquisar_animal.vazia() and not pesquisar_pessoas.vazia():
            animal = pesquisar_animal.desempilhar()
            pessoa = pesquisar_pessoas.desempilhar()

            if animal.especie == pessoa.especie_interesse:
                print(f'Animal: Espécie: {animal.especie}, Idade: {animal.idade}, Cor: {animal.cor}, Porte: {animal.porte}, Particularidade: {animal.particularidade}')
                print(f'Candidato: Nome: {pessoa.nome}, Contato: {pessoa.telefone}, Email: {pessoa.email}, Espécie de interesse: {pessoa.especie_interesse}, Preferência: {pessoa.preferencia_animal}')
