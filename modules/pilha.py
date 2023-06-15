class No:
    """
    Classe do nó.
    
    Essa classe contém uma variável para armazenar os dados chamada 'dados' e outra variável chamada 'proximo', que seria como um ponteiro que aponta para o próximo elemento e vai iniciar nulo.
    """
    def __init__(self, dados):
        self.dados = dados 
        self.proximo = None


class Pilha:
    """
    Classe da pilha.
    
    topo            - indica o topo da pilha
    vazia()         - funcão que verifica se a pilha está vazia
    empilhar()      - função que empilha no topo da pilha
    desempilhar()   - função desempilhar
    imprime()       - função que imprime de forma recursiva
    """

    def __init__(self):
        self.topo = None

    def vazia(self):
        if self.topo == None:
            return True
        else:
            return False

    def empilhar(self, dados):
        novo_elemento = No(dados)
        novo_elemento.proximo = self.topo
        self.topo = novo_elemento
    
    def desempilhar(self):
        if self.vazia():
            return None
        
        desempilhar = self.topo.dados
        self.topo = self.topo.proximo
        return desempilhar
    
    def imprime(self, No):
        if No is None:
            return
        animal = No.dados
        print(f"Tipo: {animal.tipo}, Idade: {animal.idade}, Cor: {animal.cor}, Porte: {animal.porte}, Particularidade: {animal.particularidade}")
        self.imprime(No.proximo)
