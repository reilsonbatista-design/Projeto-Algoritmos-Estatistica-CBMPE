from datetime import datetime
from ocorrencias import registrar_ocorrencia, listar_ocorrencias, filtrar_ocorrencias, salvar_ocorrencias, carregar_ocorrencias
from arvore import ArvoreBinariaBusca
from sincronizacao import adicionar_offline, sincronizar, desfazer_sincronizacao
from estatistica import executar_analise_estatistica, gerar_relatorio_estatistica
from utils import gerar_id_unico, validar_data

# carrego tudo no início
carregar_ocorrencias()

# árvore usada para ordenação
arvore = ArvoreBinariaBusca()


def mostrar_menu():
    print("\n--- Menu ---")
    print("1. Registrar Ocorrência")
    print("2. Listar Ocorrências")
    print("3. Filtrar Ocorrências")
    print("4. Sincronizar Offline")
    print("5. Exportar Relatório")
    print("6. Análise Estatística")
    print("7. Sair")
    print("8. Exportar relatório estatístico")  # nova opção


def registrar():
    # registro principal
    try:
        id = gerar_id_unico()

        tipo = input("Tipo da ocorrência: ")
        localizacao = input("Localização (Norte, Sul, Leste, Oeste): ")
        num_vitimas = int(input("Número de vítimas: "))
        recursos_usados = input("Recursos usados: ")
        descricao = input("Descrição: ")
        status = input("Status (concluída, andamento, sincronizar): ")
        data = input("Data (dd/mm/aaaa): ")

        # normalizo o tipo
        tipo_limpo = tipo.strip().lower().replace("ç", "c").replace("ã", "a").replace("é", "e")
        tipos_validos = {
            "incendio": "Incêndio",
            "resgate": "Resgate",
            "salvamento": "Salvamento",
            "acidente": "Acidente"
        }

        if tipo_limpo not in tipos_validos:
            print("Tipo inválido.")
            return

        tipo = tipos_validos[tipo_limpo]

        # normalizo localização
        loc_limpa = localizacao.strip().lower().replace("ó", "o").replace("õ", "o").replace("ã", "a")
        loc_validas = {
            "norte": "Norte",
            "sul": "Sul",
            "leste": "Leste",
            "oeste": "Oeste"
        }

        if loc_limpa not in loc_validas:
            print("Localização inválida.")
            return

        localizacao = loc_validas[loc_limpa]

        if not validar_data(data):
            print("Data inválida.")
            return

        registrar_ocorrencia(
            id, tipo, localizacao, num_vitimas,
            recursos_usados, descricao, status, data
        )

    except ValueError:
        print("Erro: digite valores válidos.")
        return


def filtrar():
    tipo = input("Tipo (ou vazio): ")
    status = input("Status (ou vazio): ")
    data = input("Data (ou vazio): ")

    filtradas = filtrar_ocorrencias(tipo, status, data)

    if filtradas.empty:
        print("Nenhuma ocorrência encontrada.")
        return

    for _, linha in filtradas.iterrows():
        print(dict(linha))


def sincronizar_offline():
    sincronizar()


def exportar_relatorio():
    salvar_ocorrencias()


def listar():
    df = listar_ocorrencias()
    if df.empty:
        print("Nenhuma ocorrência registrada.")
        return

    for _, linha in df.iterrows():
        print(dict(linha))


def rodar_estatistica():
    executar_analise_estatistica()


def menu():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            registrar()
        elif escolha == '2':
            listar()
        elif escolha == '3':
            filtrar()
        elif escolha == '4':
            sincronizar_offline()
        elif escolha == '5':
            exportar_relatorio()
        elif escolha == '6':
            rodar_estatistica()
        elif escolha == '7':
            print("Saindo...")
            break
        elif escolha == '8':
            gerar_relatorio_estatistica()
        else:
            print("Opção inválida! Tente novamente.")


menu()
