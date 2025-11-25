from ocorrencias import registrar_ocorrencia, salvar_ocorrencias

# fila offline
offline_queue = []


def adicionar_offline(ocorrencia):
    # adiciono a ocorrencia na fila
    offline_queue.append(ocorrencia)
    print(f"Ocorrência {ocorrencia['id']} adicionada à fila offline.")


def sincronizar():
    # sincronização básica
    if not offline_queue:
        print("Não há ocorrências offline para sincronizar.")
        return

    # mando cada uma para o registro normal
    for oc in offline_queue:
        registrar_ocorrencia(
            oc['id'], oc['tipo'], oc['localizacao'], oc['num_vitimas'],
            oc['recursos_usados'], oc['descricao'], oc['status'], oc['data']
        )

    offline_queue.clear()
    salvar_ocorrencias()

    print("Todas as ocorrências offline foram sincronizadas.")


def desfazer_sincronizacao():
    # remove a última da fila
    if not offline_queue:
        print("Nenhuma ocorrência offline para desfazer.")
        return

    removida = offline_queue.pop()
    print(f"Ocorrência {removida['id']} removida da fila offline.")
