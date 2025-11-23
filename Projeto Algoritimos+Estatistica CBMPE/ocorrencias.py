import pandas as pd

# Lista para armazenar as ocorrências (simula um banco de dados)
ocorrencias = pd.DataFrame()

def carregar_ocorrencias():
    """
    Função para carregar as ocorrências a partir do arquivo `dados.json`.
    Agora, as ocorrências são armazenadas em um DataFrame do Pandas.
    """
    global ocorrencias
    try:
        # Carrega o arquivo JSON no DataFrame
        ocorrencias = pd.read_json('dados.json')
        print("Ocorrências carregadas com sucesso.")
    except FileNotFoundError:
        print("Arquivo dados.json não encontrado. Nenhuma ocorrência carregada.")
        ocorrencias = pd.DataFrame()  # Cria um DataFrame vazio se não houver dados

def salvar_ocorrencias():
    """
    Função para salvar as ocorrências no arquivo `dados.json`.
    Salva os dados no formato JSON usando Pandas.
    """
    if not ocorrencias.empty:
        # Salva o DataFrame como um arquivo JSON
        ocorrencias.to_json('dados.json', orient='records', lines=True)
        print("Ocorrências salvas com sucesso no arquivo dados.json.")
    else:
        print("Nenhuma ocorrência para salvar.")

def registrar_ocorrencia(id, tipo, localizacao, num_vitimas, recursos_usados, descricao, status, data):
    """
    Função para registrar uma nova ocorrência na lista de ocorrências.
    """
    global ocorrencias

    # Verificar se o id já existe
    if id in ocorrencias['id'].values:
        print(f"Erro: Ocorrência com ID {id} já registrada.")
        return

    # Cria um dicionário para a nova ocorrência
    ocorrencia = {
        'id': id,
        'tipo': tipo,
        'localizacao': localizacao,
        'num_vitimas': num_vitimas,
        'recursos_usados': recursos_usados,
        'descricao': descricao,
        'status': status,
        'data': data
    }

    # Adiciona a nova ocorrência ao DataFrame
    ocorrencias = ocorrencias.append(ocorrencia, ignore_index=True)
    print(f"Ocorrência {id} registrada com sucesso.")
    
    # Salvar as ocorrências após o registro
    salvar_ocorrencias()

def listar_ocorrencias():
    """
    Função para listar todas as ocorrências registradas.
    """
    return ocorrencias

def filtrar_ocorrencias(tipo=None, status=None, data=None):
    """
    Função para filtrar as ocorrências com base em tipo, status e data.
    """
    filtradas = ocorrencias
    if tipo:
        filtradas = filtradas[filtradas['tipo'] == tipo]
    if status:
        filtradas = filtradas[filtradas['status'] == status]
    if data:
        filtradas = filtradas[filtradas['data'] == data]
    
    return filtradas

