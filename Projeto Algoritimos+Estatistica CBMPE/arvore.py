class No:
    def __init__(self, ocorrencia):
        self.ocorrencia = ocorrencia  # A ocorrência é um dicionário com os dados da ocorrência
        self.esquerda = None  # Subárvore à esquerda
        self.direita = None  # Subárvore à direita

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # Função para inserir uma nova ocorrência na árvore
    def inserir(self, ocorrencia):
        if self.raiz is None:
            self.raiz = No(ocorrencia)
        else:
            self._inserir_recursivo(self.raiz, ocorrencia)

    def _inserir_recursivo(self, no, ocorrencia):
        if ocorrencia['id'] < no.ocorrencia['id']:
            # Se o ID for menor, vai para a subárvore à esquerda
            if no.esquerda is None:
                no.esquerda = No(ocorrencia)
            else:
                self._inserir_recursivo(no.esquerda, ocorrencia)
        else:
            # Se o ID for maior ou igual, vai para a subárvore à direita
            if no.direita is None:
                no.direita = No(ocorrencia)
            else:
                self._inserir_recursivo(no.direita, ocorrencia)

    # Função para listar todas as ocorrências em ordem
    def listar(self):
        return self._listar_recursivo(self.raiz)

    def _listar_recursivo(self, no):
        if no is None:
            return []
        # Listar ocorrências na subárvore à esquerda, no nó atual e depois na subárvore à direita
        return self._listar_recursivo(no.esquerda) + [no.ocorrencia] + self._listar_recursivo(no.direita)

    # Função para filtrar ocorrências por localização
    def filtrar_por_localizacao(self, localizacao):
        return self._filtrar_recursivo(self.raiz, localizacao)

    def _filtrar_recursivo(self, no, localizacao):
        if no is None:
            return []
        resultado = []
        if no.ocorrencia['localizacao'] == localizacao:
            resultado.append(no.ocorrencia)
        # Busca recursiva nas subárvores
        resultado += self._filtrar_recursivo(no.esquerda, localizacao)
        resultado += self._filtrar_recursivo(no.direita, localizacao)
        return resultado

    # Função para remover uma ocorrência pelo ID
    def remover(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, no, id):
        if no is None:
            return no

        if id < no.ocorrencia['id']:
            # ID menor que o do nó, vai para a subárvore esquerda
            no.esquerda = self._remover_recursivo(no.esquerda, id)
        elif id > no.ocorrencia['id']:
            # ID maior que o do nó, vai para a subárvore direita
            no.direita = self._remover_recursivo(no.direita, id)
        else:
            # Nó a ser removido encontrado
            if no.esquerda is None:
                # Nó sem filho à esquerda
                return no.direita
            elif no.direita is None:
                # Nó sem filho à direita
                return no.esquerda
            else:
                # Nó com dois filhos: pegar o menor nó da subárvore direita
                no.ocorrencia = self._minimo(no.direita).ocorrencia
                # Remover o nó substituto
                no.direita = self._remover_recursivo(no.direita, no.ocorrencia['id'])

        return no

    def _minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
