📘 Sistema de Registro de Ocorrências – CBMPE

Projeto acadêmico – Python (Estruturas de Dados + Estatística)

Este sistema simula o back-end de um aplicativo do Corpo de Bombeiros Militar de Pernambuco (CBMPE), permitindo registrar ocorrências, filtrar, gerar estatísticas, sincronizar dados offline e exportar relatórios profissionais.

O projeto foi desenvolvido utilizando estruturas de dados, programação modular, tratamento de erros, árvore binária de busca, fila offline, Pandas, NumPy e estatística aplicada.

📂 Funcionalidades Principais
🔥 Registro de Ocorrências

Cadastro completo de uma ocorrência

Padronização automática de digitação (incêndio, resgate, etc.)

Correção de maiúsculas, acentos e erros comuns

Validação de data (dd/mm/aaaa)

Salvamento automático no arquivo dados.json

📋 Listagem e Filtros

Listar todas as ocorrências salvas

Filtrar por:

Tipo

Status

Data

🌳 Árvore Binária de Busca (ABB)

As ocorrências também são armazenadas em uma árvore binária, utilizada para organizar e listar dados de forma ordenada.

📡 Modo Offline + Sincronização

O sistema possui:

Fila offline para guardar ocorrências quando não há internet

Sincronização automática com a base principal

Funções:

adicionar_offline()

sincronizar()

desfazer_sincronizacao()

📊 Análise Estatística (Estatística Descritiva)

Utiliza os valores de num_vitimas para calcular:

Média

Mediana

Moda

Variância

Desvio Padrão

Interpretação automática

Além disso:

✔ exibe tudo formatado no terminal
✔ gera relatório profissional para impressão ou envio

📄 Geração de Relatório Estatístico (TXT)

O relatório completo fica salvo em:

/relatorios/relatorio_estatistica.txt


Ele contém:

Dados analisados

Tendência central

Medidas de dispersão

Interpretação final

Pronto para apresentação ou anexação em documentos oficiais.

🧩 Estrutura do Projeto
📁 projeto/
│
├── main.py                # menu principal
├── ocorrencias.py         # CRUD das ocorrências + DF + árvore
├── arvore.py              # árvore binária de busca
├── sincronizacao.py       # fila offline + sincronização
├── estatistica.py         # análise estatística + relatório
├── utils.py               # funções auxiliares
│
├── dados.json             # armazenamento das ocorrências
│
└── /relatorios/           # relatórios automáticos
    └── relatorio_estatistica.txt

▶️ Como Executar o Projeto

Certifique-se de ter Python instalado (3.8+)

Instale dependências:

pip install pandas numpy


Execute o sistema:

python main.py


Use o menu interativo:

--- Menu ---
1. Registrar Ocorrência
2. Listar Ocorrências
3. Filtrar Ocorrências
4. Sincronizar Offline
5. Exportar Relatório
6. Análise Estatística
7. Sair
8. Exportar relatório estatístico

📌 Tecnologias e Conceitos Utilizados

Python 3

Pandas (armazenamento e filtros)

NumPy (estatística)

Estruturas de dados:

Lista

Dicionário

Fila

Árvore Binária de Busca

Tratamento de exceções

Normalização de strings

Validação de dados

Arquivos JSON

Geração de relatórios TXT

Programação modular

✅ Objetivo Acadêmico

O projeto atende aos requisitos de:

✔ Estruturas de dados
✔ Persistência de dados
✔ Funções e modularização
✔ Estatísticas descritivas
✔ Manipulação de texto e JSON
✔ Boas práticas de programação

👨‍🚒 Exemplo de Saída da Análise Estatística
===== ANÁLISE ESTATÍSTICA DAS OCORRÊNCIAS =====

Valores utilizados (n vítimas): [2, 5, 3]
Total analisado: 3

--- Tendência Central ---
Média: 3.33
Mediana: 3.00
Moda: Amodal
-------------------------

--- Dispersão ---
Variância: 2.33
Desvio Padrão: 1.52
------------------
===============================================

📝 Licença

Uso acadêmico e educacional.
Pode ser utilizado, modificado e apresentado livremente.
