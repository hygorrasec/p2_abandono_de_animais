#cabeçalho
def cabecalho(txt):
    print('\033[1;90m=\033[m'*45)
    print(txt.center(45))
    print('\033[1;90m=\033[m'*45)


#verificando se o nome é só letra
def is_alpha_space(str):
    return all(char.isalpha() or char.isspace() for char in str)

#validar nome
def validar_nome(n):
    while True:
        s1 = input(f'{n}').upper()

        if not (is_alpha_space(s1) and len(s1) >4):
            print('\033[0;31mValores inválidos ou nome curto demais.\033[m')
        else:
            return s1


def validar_tel(tel):
    while True:
        if len(tel) > 0 and len(tel) < 12:
            return all(c.isdigit()  for c in tel)
        else:
            print('\033[0;31mFormato invalido.\033[m')
    
#validando inteiro
def verificar_opcao(msg,msg1):
    while True:
        try:
            v = int(input(f'{msg}'))
            if v > 0 and v < 5:
                return v
            else:
                print('\033[0;31mIforme apenas os números de 1 a 5.\033[m')
                
        except:
            print(f'{msg1}')
            


def Idade():
    while True:
        try:
            idade = int(input('Informe sua idade: '))
            if (idade > 0 ):
                return idade
        except:
            print('Dados invalidos.')
            