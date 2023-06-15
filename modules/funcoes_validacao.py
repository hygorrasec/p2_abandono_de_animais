def cabecalho(txt):
    """
    Função para imprimir cabeçalho.
    """
    print(txt.center(45))

def is_alpha_space(str):
    """
    Função para verificar se a string contém apenas letras e espaços.
    """
    return all(char.isalpha() or char.isspace() for char in str)


def validar_nome(n):
    """
    Função para validar nome.
    """
    while True:
        s1 = input(f'{n}').upper()

        if not (is_alpha_space(s1) and len(s1) >4):
            print('\033[0;31mValores inválidos ou nome curto demais.\033[m')
        else:
            return s1


def validar_tel(tel):
    """
    Função para validar telefone.
    """
    while True:
        if len(tel) > 0 and len(tel) < 12:
            return all(c.isdigit()  for c in tel)
        else:
            print('\033[0;31mFormato invalido.\033[m')


def verificar_opcao(msg, msg1):
    """
    Função para verificar opção.
    """
    while True:
        try:
            v = int(input(f'{msg}'))
            if v >= 1 and v <= 6:
                return v
            else:
                print('\033[0;31mInforme apenas os números de 1 a 6.\033[m')
                
        except:
            print(f'{msg1}')
            

def Idade():
    """
    Função para validar idade.
    """
    while True:
        try:
            idade = int(input('Informe sua idade: '))
            if (idade > 0 ):
                return idade
        except:
            print('Dados invalidos.')
