import statistics
import numpy as np

def executar_analise_estatistica(dados_ocorrencias=None):
    if dados_ocorrencias is None:
        ocorrencias = [50, 120, 30, 80]
        print("AVISO: Usando dados de exemplo para a análise estatística.")
    else:
        # Se você tiver uma maneira de extrair os totais de ocorrências da sua Árvore, use aqui.
        # Por simplicidade, ainda usaremos o exemplo. Se a sua lógica de dados for alterada,
        # esta parte deve ser ajustada.
        ocorrencias = dados_ocorrencias 
        
    n = len(ocorrencias)

    if n == 0:
        print("Não há dados de ocorrências para realizar a análise estatística.")
        return

    print("\nOCORRÊNCIAS DE BOMBEIROS")
    print(f"Conjunto de Dados (Total de Ocorrências por Tipo): {ocorrencias}")
    print(f"Número de Observações (n): {n}\n")

    media = sum(ocorrencias) / n
    mediana = statistics.median(ocorrencias)

    try:
        moda = statistics.mode(ocorrencias)
        moda_str = str(moda)
    except statistics.StatisticsError:
        moda_str = "Amodal"

    print("--- Medidas de Tendência Central ---")
    print(f"1. Média: {media:.2f}")
    print(f"2. Mediana: {mediana:.2f}")
    print(f"3. Moda: {moda_str}")
    print("-" * 35)

    if n > 1:
        variancia = np.var(ocorrencias, ddof=1)
        desvio_padrao = np.std(ocorrencias, ddof=1)

        print("--- Medidas de Dispersão ---")
        print(f"1. Variância Amostral (σ²): {variancia:.2f}")
        print(f"2. Desvio Padrão Amostral (σ): {desvio_padrao:.2f}")
        print("-" * 35)

        print("\nResumo e Interpretação")
        print(f"Média: {media:.2f} | Mediana: {mediana:.2f} | Desvio Padrão: {desvio_padrao:.2f}")
        print("\n**Conclusão do Desvio Padrão:**")
        print(f"O Desvio Padrão ({desvio_padrao:.2f}) é alto em relação à Média ({media:.2f}),")
        print("o que indica uma alta dispersão nos dados.")
    else:
        print("Não é possível calcular Variância ou Desvio Padrão com apenas uma observação.")