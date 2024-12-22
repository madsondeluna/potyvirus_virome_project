# Processamento de Tabelas de Genomas de Potivyrus

Este repositório contém um script em Python para processar tabelas de genomas virais, realizando filtragem, remoção de redundâncias e gerando relatórios detalhados.

## Funcionalidades

O script realiza as seguintes etapas:

1. **Carregar Tabela Original**:
   - Carrega a tabela de genomas a partir de um arquivo `.tsv`.
   - Salva a tabela original em formato `.csv` para referência.

2. **Filtragem de Genomas Completos**:
   - Filtra a tabela para manter apenas os registros cujo valor na coluna `Level` seja `"Complete Genome"`.
   - Salva a tabela filtrada em formato `.csv`.

3. **Remoção de Redundâncias**:
   - Identifica espécies redundantes na coluna `Organism Scientific Name`.
   - Mantém apenas o registro com o maior valor na coluna `Size` para cada espécie.
   - Salva a tabela final (sem redundâncias) em formato `.csv`.

4. **Relatório Detalhado**:
   - Gera um arquivo de texto (`detailed_filtering.txt`) com informações sobre as etapas de processamento:
     - Número de registros em cada etapa.
     - Quantidade de registros removidos em cada etapa.
     - Média dos valores da coluna `Size` na tabela final (não redundante).

## Estrutura do Repositório

```
.
├── data_summary.tsv         # Exemplo de arquivo de entrada (substitua pelo seu arquivo)
├── process_genomes.py       # Script principal
├── README.md                # Este arquivo
└── Outputs                  # Diretório para os arquivos gerados
    ├── tabela_original.csv
    ├── tabela_filtrada_complete_genome.csv
    ├── tabela_nao_redundante.csv
    ├── detailed_filtering.txt
```

## Requisitos

- Python 3.x
- Bibliotecas:
  - `pandas`

Para instalar as dependências, execute:
```bash
pip install pandas
```

## Como Usar

1. **Prepare o Arquivo de Entrada**:
   - Substitua o caminho do arquivo `file_name` no script para o caminho do seu arquivo `.tsv`.

2. **Execute o Script**:
   - Salve o script como `process_genomes.py`.
   - Execute no terminal:
     ```bash
     python process_genomes.py
     ```

3. **Arquivos Gerados**:
   - O script irá gerar os seguintes arquivos no diretório de execução:
     - `tabela_original.csv`: Tabela original carregada.
     - `tabela_filtrada_complete_genome.csv`: Tabela filtrada para incluir apenas genomas completos.
     - `tabela_nao_redundante.csv`: Tabela final sem redundâncias.
     - `detailed_filtering.txt`: Relatório detalhado do processamento.

## Exemplos de Saída

### Relatório (`detailed_filtering.txt`)
```
Etapa 1: Arquivo original carregado com 225 registros.
Etapa 2: Após filtrar apenas 'Complete Genome', restaram 174 registros. Foram removidos 51 registros.
Etapa 3: Após remover redundâncias, restaram 158 registros. Foram removidos 16 registros.
Média do 'Size' na tabela final (não redundante): 1234.56
```

### Estrutura da Tabela Final (`tabela_nao_redundante.csv`)
| Organism Scientific Name | Assembly Accession | Size  |
|---------------------------|--------------------|-------|
| Species A                | ACC123             | 56789 |
| Species B                | ACC456             | 12345 |

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
