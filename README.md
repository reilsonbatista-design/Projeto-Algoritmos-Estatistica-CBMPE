Sistema de Registro de Ocorrências – CBMPE

Este projeto simula o sistema interno usado para registrar ocorrências operacionais do Corpo de Bombeiros Militar de Pernambuco (CBMPE).
O objetivo é demonstrar o uso de estruturas de dados, organização modular, estatística e processamento de informações.

Funcionalidades do Sistema
1. Registro de ocorrências

O usuário pode cadastrar uma ocorrência informando:

tipo (Incêndio, Resgate, Salvamento, Acidente)

localização (Norte, Sul, Leste, Oeste)

número de vítimas

recursos usados

descrição

status (concluída, andamento, sincronizar)

data

O sistema corrige automaticamente erros de digitação (acentos e maiúsculas/minúsculas).

2. Listagem

Exibe todas as ocorrências armazenadas no sistema.

3. Filtros

O usuário pode filtrar ocorrências por:

tipo

status

data

4. Árvore Binária

As ocorrências também são organizadas em uma árvore binária para permitir listagem ordenada.

5. Fila Offline

O sistema simula o modo offline usando uma fila:

adiciona ocorrências offline

sincroniza com a base principal

permite desfazer a última adição offline

6. Estatística

Com base no número de vítimas, o sistema calcula:

média

mediana

moda

variância

desvio padrão

Tudo é exibido no terminal de forma organizada.

7. Relatório Estatístico

Ao selecionar a opção correspondente, o sistema gera um arquivo:

relatorios/relatorio_estatistica.txt


Com um resumo profissional contendo:

valores analisados

tendência central

dispersão

interpretação final

Esse relatório pode ser enviado ou apresentado.

8. Exportação

As ocorrências são salvas no arquivo:

dados.json

Estrutura do Projeto
main.py                    -> menu do sistema
ocorrencias.py             -> sistema principal de cadastro
arvore.py                  -> árvore binária de busca
sincronizacao.py           -> fila offline e sincronização
estatistica.py             -> estatística + relatório
utils.py                   -> funções extras
dados.json                 -> banco de dados
/relatorios/               -> relatório estatístico

Como Executar

Instale as dependências:

pip install pandas numpy


Execute o programa:

python main.py

Tecnologias Usadas

Python 3

Pandas

NumPy

Estruturas de dados (lista, dicionário, fila, árvore binária)

JSON

Estatística descritiva

Objetivo do Projeto

Atender aos requisitos acadêmicos envolvendo:

estruturas de dados

modularização

análise estatística

persistência de dados

bom uso de funções
