from datetime import datetime
from ocorrencias import registrar_ocorrencia, listar_ocorrencias, filtrar_ocorrencias, salvar_ocorrencias, carregar_ocorrencias
from arvore import ArvoreBinariaBusca
from sincronizacao import adicionar_offline, sincronizar, desfazer_sincronizacao
from utils import validar_data, gerar_id_unico


# Carregar dados ao iniciar
carregar_ocorrencias()

# Criando a árvore para armazenar as ocorrências
arvore = ArvoreBinariaBusca()

def mostrar_menu():
  print("\n--- Menu ---")
  print("1. Registrar Ocorrência")
  print("2. Listar Ocorrências")
  print("3. Filtrar Ocorrências")
  print("4. Sincronizar Offline")
  print("5. Exportar Relatório")
  print("6. Sair")

def registrar():
  id = gerar_id_unico()
  tipo = input("Tipo da ocorrência: ")
  localizacao = input("Localização (Norte, Sul, Leste, Oeste): ")
  num_vitimas = int(input("Número de vítimas: "))
  recursos_usados = input("Recursos usados: ")
  descricao = input("Descrição: ")
  status = input("Status (concluída, andamento, sincronizar): ")
  data = input("Data (dd/mm/aaaa): ")

  if not validar_data(data):
      print("Data inválida! Use o formato dd/mm/aaaa.")
      return

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

  arvore.inserir(ocorrencia)
  print(f"Ocorrência {id} registrada com sucesso.")


def filtrar():
  tipo = input("Digite o tipo da ocorrência para filtrar (ou deixe em branco para todos): ")
  status = input("Digite o status da ocorrência para filtrar (ou deixe em branco para todos): ")
  data = input("Digite a data da ocorrência para filtrar (dd/mm/aaaa, ou deixe em branco para todos): ")

  filtradas = filtrar_ocorrencias(tipo,status,data)

  if not filtradas:
    print("Nenhuma ocorrência encontrada com os filtros especificados.")

  for ocorrencia in filtradas:
    print(ocorrencia)

def sincronizar_offline():
  sincronizar()
  print("Sincronização completa.")

def exportar_relatorio():
  salvar_ocorrencias()
  print("Relatório exportado com sucesso.")

def listar():
  ocorrencias = arvore.listar()
  if not ocorrencias:
    print("Nenhuma ocorrência registrada.")
  for ocorrencia in ocorrencias:
      print(ocorrencia)



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
      print("Saindo...")
      break
    else:
      print("Opção inválida! Tente novamente.")

menu()