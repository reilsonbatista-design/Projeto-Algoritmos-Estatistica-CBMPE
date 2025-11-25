import statistics
import numpy as np

ocorrencias = [50, 120, 30, 80]
n = len(ocorrencias)

print("OCORRÊNCIAS DE BOMBEIROS\n")
print(f"Conjunto de Dados: {ocorrencias}")
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

variancia = np.var(ocorrencias, ddof=1)
desvio_padrao = np.std(ocorrencias, ddof=1)

print("--- Medidas de Dispersão ---")
print(f"1. Variância Amostral (σ²): {variancia:.2f}")
print(f"2. Desvio Padrão Amostral (σ): {desvio_padrao:.2f}")
print("-" * 35)

print(f"Média: {media:.2f} | Mediana: {mediana:.2f} | Desvio Padrão: {desvio_padrao:.2f}")
print("\nConclusão do Desvio Padrão:")
print(f"O Desvio Padrão ({desvio_padrao:.2f}) é alto em relação à Média ({media:.2f}),")
print("o que indica uma alta dispersão. Os tipos de ocorrências (como Resgate: 120 e")
print("Salvamento: 30) variam significativamente do volume médio de 70, sugerindo uma")
print("distribuição não uniforme do foco operacional.")