import statistics
import numpy as np
import pandas as pd
import os
from ocorrencias import listar_ocorrencias


def executar_analise_estatistica(dados_ocorrencias=None):
    # se não passar valores direto, eu puxo do DF
    if dados_ocorrencias is None:
        df = listar_ocorrencias()

        if df is None or df.empty:
            print("Não há dados para análise estatística.")
            return None  # retorno aqui pq vou usar essa info pra gerar relatório

        # verifico se existe a coluna certa
        if 'num_vitimas' not in df.columns:
            print("A coluna 'num_vitimas' não foi encontrada.")
            return None

        # limpo valores errados só pra garantir
        df = df[pd.to_numeric(df['num_vitimas'], errors='coerce').notnull()]

        ocorrencias = df['num_vitimas'].astype(int).tolist()
    else:
        ocorrencias = dados_ocorrencias

    n = len(ocorrencias)

    if n == 0:
        print("Não há dados suficientes para análise.")
        return None

    # cálculos principais
    media = sum(ocorrencias) / n
    mediana = statistics.median(ocorrencias)

    try:
        moda = statistics.mode(ocorrencias)
        moda_str = str(moda)
    except statistics.StatisticsError:
        moda_str = "Amodal"

    # variância só se tiver mais de 1
    if n > 1:
        variancia = np.var(ocorrencias, ddof=1)
        desvio = np.std(ocorrencias, ddof=1)
    else:
        variancia = None
        desvio = None

    # saída bonitinha no terminal
    print("\n===== ANÁLISE ESTATÍSTICA DAS OCORRÊNCIAS =====")
    print(f"\nValores utilizados (n vítimas): {ocorrencias}")
    print(f"Total analisado: {n}\n")

    print("--- Tendência Central ---")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda_str}")
    print("-------------------------")

    if variancia is not None:
        print("\n--- Dispersão ---")
        print(f"Variância: {variancia:.2f}")
        print(f"Desvio Padrão: {desvio:.2f}")
        print("------------------")
    else:
        print("\nSomente um valor disponível. Sem desvio padrão.")
    
    print("===============================================\n")

    # retorno tudo para gerar relatório depois
    return {
        "dados": ocorrencias,
        "n": n,
        "media": media,
        "mediana": mediana,
        "moda": moda_str,
        "variancia": variancia,
        "desvio": desvio
    }


def gerar_relatorio_estatistica():
    # gero os dados para o relatório
    resultado = executar_analise_estatistica()

    if resultado is None:
        print("Não foi possível gerar relatório estatístico.")
        return

    # crio pasta relatorios se não existir
    if not os.path.exists("relatorios"):
        os.makedirs("relatorios")

    caminho = "relatorios/relatorio_estatistica.txt"

    # escrevo o arquivo todo
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO ESTATÍSTICO - OCORRÊNCIAS CBMPE\n\n")
        f.write(f"Quantidade de registros analisados: {resultado['n']}\n")
        f.write(f"Valores utilizados (número de vítimas): {resultado['dados']}\n\n")

        f.write("--- Tendência Central ---\n")
        f.write(f"Média: {resultado['media']:.2f}\n")
        f.write(f"Mediana: {resultado['mediana']:.2f}\n")
        f.write(f"Moda: {resultado['moda']}\n\n")

        if resultado['variancia'] is not None:
            f.write("--- Dispersão ---\n")
            f.write(f"Variância: {resultado['variancia']:.2f}\n")
            f.write(f"Desvio Padrão: {resultado['desvio']:.2f}\n\n")
        else:
            f.write("Somente um valor disponível. Sem variância.\n\n")

        f.write("Interpretação:\n")
        if resultado['variancia'] is not None:
            f.write(
                "O desvio padrão mostra quanto o número de vítimas varia "
                "entre as ocorrências registradas.\n"
            )
        else:
            f.write("Com apenas um valor não é possível avaliar variação.\n")

    print(f"Relatório gerado em: {caminho}")
