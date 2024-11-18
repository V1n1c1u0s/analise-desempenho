class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self, valores_iniciais=None):
        self.head = None
        if valores_iniciais:
            for valor in valores_iniciais:
                self.adicionar(valor)

    def adicionar(self, valor):
        novo_nodo = Nodo(valor)
        if not self.head:
            self.head = novo_nodo
        else:
            # Atravessa a lista para encontrar a última posição
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def remover(self, valor):
        atual = self.head
        anterior = None

        while atual:
            if atual.valor == valor:
                if anterior:  # Se não for o primeiro nodo
                    anterior.proximo = atual.proximo
                else:  # Se for o primeiro nodo
                    self.head = atual.proximo
                return  # A remoção foi realizada, retornamos
            anterior = atual
            atual = atual.proximo

        # Caso o valor não seja encontrado, não faz nada
        print(f"Valor {valor} não encontrado para remoção.")

    def imprimir(self):
        atual = self.head
        lista = []
        while atual:
            lista.append(str(atual.valor))
            atual = atual.proximo
        print("Lista:", " -> ".join(lista))

    def adicionar_posicao(self, valor, posicao):
        novo_nodo = Nodo(valor)
        if posicao == 0:  # Adicionar no início
            novo_nodo.proximo = self.head
            self.head = novo_nodo
            return
        
        atual = self.head
        indice = 0
        while atual and indice < posicao - 1:
            atual = atual.proximo
            indice += 1
        
        if atual:  # Inserir após o nodo atual
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo
        else:
            print(f"Posição {posicao} fora do alcance. Não foi possível adicionar.")

    def remover_posicao(self, posicao):
        if posicao == 0:
            if self.head:
                self.head = self.head.proximo
            else:
                print("Lista vazia.")
            return
        
        atual = self.head
        anterior = None
        indice = 0
        while atual and indice < posicao:
            anterior = atual
            atual = atual.proximo
            indice += 1
        
        if atual:
            anterior.proximo = atual.proximo
        else:
            print(f"Posição {posicao} fora do alcance. Não foi possível remover.")

# Função que lê o arquivo e executa as operações
def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Leitura inicial da lista
    lista_inicial = list(map(int, linhas[0].strip().split()))
    lista = ListaEncadeada(lista_inicial)

    # Número de ações
    num_acoes = int(linhas[1].strip())

    # Processando as ações
    for i in range(2, 2 + num_acoes):
        acao = linhas[i].strip().split()

        # Ignorar linhas em branco ou mal formatadas
        if len(acao) < 2 and acao[0] != "P":
            print(f"Ação mal formatada ou linha vazia ignorada: {linhas[i].strip()}")
            continue

        nome_acao = acao[0]
        
        # Processando as ações
        if nome_acao == "A":
            numero = int(acao[1])
            posicao = int(acao[2])  # Pega a posição para a ação de adicionar
            lista.adicionar_posicao(numero, posicao)
        elif nome_acao == "R":
            numero = int(acao[1])
            lista.remover(numero)  # Agora só passamos o número para remoção
        elif nome_acao == "P":
            lista.imprimir()  # Chama imprimir sem argumentos adicionais

# Exemplo de execução
if __name__ == "__main__":
    processar_arquivo("arq.txt")
