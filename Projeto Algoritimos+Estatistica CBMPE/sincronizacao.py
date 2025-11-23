from ocorrencias import registrar_ocorrencia

# Fila para armazenar as ocorrências offline (simulando o armazenamento temporário)
offline_queue = []

def adicionar_offline(ocorrencia):
    """
    Função para adicionar uma ocorrência na fila de ocorrências offline.
    """
    offline_queue.append(ocorrencia)
    print(f"Ocorrência {ocorrencia['id']} adicionada à fila offline.")

def sincronizar():
    """
    Função para sincronizar as ocorrências offline com a lista principal.
    As ocorrências na fila offline serão movidas para o banco de dados principal.
    """
    if not offline_queue:
        print("Não há ocorrências offline para sincronizar.")
        return

    for ocorrencia in offline_queue:
        # Registra cada ocorrência na árvore principal (DataFrame de ocorrências)
        registrar_ocorrencia(
            ocorrencia['id'],
            ocorrencia['tipo'],
            ocorrencia['localizacao'],
            ocorrencia['num_vitimas'],
            ocorrencia['recursos_usados'],
            ocorrencia['descricao'],
            ocorrencia['status'],
            ocorrencia['data']
        )
      
    # Após a sincronização, limpa a fila offline
    offline_queue.clear()
    print("Todas as ocorrências offline foram sincronizadas com sucesso.")

def desfazer_sincronizacao():
    """
    Função para desfazer a sincronização de uma ocorrência.
    Remove a última ocorrência da fila offline.
    """
    if not offline_queue:
        print("Não há ocorrências na fila offline para desfazer.")
        return

    ocorrencia_removida = offline_queue.pop()
    print(f"Sincronização da ocorrência {ocorrencia_removida['id']} foi desfeita.")
