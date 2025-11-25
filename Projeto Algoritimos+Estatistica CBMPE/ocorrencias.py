import pandas as pd
from arvore import ArvoreBinariaBusca  # uso a árvore para manter ordem

# dataframe principal
colunas_ocorrencias = ['id', 'tipo', 'localizacao', 'num_vitimas',
                       'recursos_usados', 'descricao', 'status', 'data']
ocorrencias = pd.DataFrame(columns=colunas_ocorrencias)

# instância da árvore
arvore = ArvoreBinariaBusca()


def carregar_ocorrencias():
    # carrega tudo do json pro dataframe e monta a árvore de novo
    global ocorrencias
    try:
        ocorrencias = pd.read_json('dados.json', lines=True)

        # reinserindo todas as ocorrencias na árvore
        for _, linha in ocorrencias.iterrows():
            arvore.inserir(linha.to_dict())

    except FileNotFoundError:
        ocorrencias = pd.DataFrame(columns=colunas_ocorrencias)
    except ValueError:
        ocorrencias = pd.DataFrame(columns=colunas_ocorrencias)


def salvar_ocorrencias():
    # salvo o DF inteiro no json
    if ocorrencias.empty:
        print("Nenhuma ocorrência para salvar.")
        return

    ocorrencias.to_json('dados.json', orient='records', lines=True)
    print("Ocorrências salvas com sucesso.")


def registrar_ocorrencia(id, tipo, localizacao, num_vitimas,
                         recursos_usados, descricao, status, data):
    # registro principal
    global ocorrencias

    # normalizo status para evitar erro de digitação
    status = status.strip().lower().replace("í", "i").replace("á", "a").replace("é", "e").replace("ã", "a")

    status_validos = {
        "concluida": "concluída",
        "andamento": "andamento",
        "sincronizar": "sincronizar"
    }

    if status not in status_validos:
        print("Status inválido. Use: concluída / andamento / sincronizar.")
        return

    status = status_validos[status]

    # impede duplicação
    if 'id' in ocorrencias.columns and id in ocorrencias['id'].values:
        print(f"Erro: Ocorrência com ID {id} já registrada.")
        return

    # valida número de vítimas
    if not isinstance(num_vitimas, int) or num_vitimas < 0:
        print("Número de vítimas inválido.")
        return

    # montagem do dicionário da ocorrência
    nova = {
        'id': id,
        'tipo': tipo,
        'localizacao': localizacao,
        'num_vitimas': num_vitimas,
        'recursos_usados': recursos_usados,
        'descricao': descricao,
        'status': status,
        'data': data
    }

    # adiciono no DF
    nova_linha = pd.DataFrame([nova])
    ocorrencias = pd.concat([ocorrencias, nova_linha], ignore_index=True)

    # adiciono também na árvore
    arvore.inserir(nova)

    print(f"Ocorrência {id} registrada com sucesso.")
    salvar_ocorrencias()


def listar_ocorrencias():
    # retorno o DF inteiro
    return ocorrencias


def filtrar_ocorrencias(tipo=None, status=None, data=None):
    # filtro básico usando DF
    filtradas = ocorrencias

    if tipo:
        filtradas = filtradas[filtradas['tipo'] == tipo]
    if status:
        filtradas = filtradas[filtradas['status'] == status]
    if data:
        filtradas = filtradas[filtradas['data'] == data]

    return filtradas
