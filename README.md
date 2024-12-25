# Processamento de Tabelas de Genomas de Potivyrus

Este repositório contém scripts em Python para processar tabelas de genomas virais, realizando filtragem, remoção de redundâncias, geração de relatórios detalhados e clusterização de genomas.

## Aviso

**Este projeto está em desenvolvimento.** Novas etapas e funcionalidades estão sendo planejadas e serão adicionadas futuramente.

## Funcionalidades

### 1. Processamento Inicial

O script `process_genomes.py` realiza as seguintes etapas:

1. **Carregar Tabela Original**:
   - Carrega a tabela de genomas a partir de um arquivo `.tsv` obtido no NCBI ao baixar os genomas de escolha compactados em `zip`.
   - Salva a tabela original em formato `.csv` para referência.

2. **Filtragem de Genomas Completos**:
   - Filtra a tabela para manter apenas os registros cujo valor na coluna `Level` seja `"Complete Genome"`.
   - Salva a tabela filtrada em formato `.csv`.

3. **Remoção de Redundâncias**:
   - Identifica espécies redundantes na coluna `Organism Scientific Name`.
   - Mantém apenas o registro com o maior valor na coluna `Size` (tamanho do genoma) para cada espécie.
   - Salva a tabela final (sem redundâncias) em formato `.csv`.

4. **Relatório Detalhado**:
   - Gera um arquivo de texto (`detailed_filtering.txt`) com informações sobre as etapas de processamento:
     - Número de registros em cada etapa.
     - Quantidade de registros removidos em cada etapa.
     - Média dos valores da coluna `Size` (tamanho do genoma) na tabela final (não redundante).

### 2. Clusterização de Genomas

O script `genome_clustering.py` realiza a clusterização dos genomas não redundantes e completos, gerando um gráfico.

1. **Carregar Tabela Não Redundante**:
   - Carrega o arquivo `tabela_nao_redundante.csv` gerado pelo script anterior.

2. **Clusterização com K-means**:
   - Normaliza os tamanhos dos genomas para realizar a clusterização.
   - Aplica o algoritmo K-means para identificar clusters com base no tamanho dos genomas.

3. **Geração de Gráfico**:
   - Cria um gráfico de dispersão, colorido de acordo com os clusters identificados.
   - Salva e exibe o gráfico como resultado.

### 3, Coming next... 

## Estrutura do Repositório

```
.
├── data_summary.tsv         # Exemplo de arquivo de entrada (Atenção: Substitua pelo seu arquivo!)
├── process_genomes.py       # Script principal para processamento inicial
├── genome_clustering.py     # Script para clusterização de genomas
├── README.md                # Este arquivo
└── Outputs                  # Diretório para os arquivos gerados
    ├── tabela_original.csv
    ├── tabela_filtrada_complete_genome.csv
    ├── tabela_nao_redundante.csv
    ├── detailed_filtering.txt
    ├── clustering_plot.png  # Gráfico gerado pelo script de clusterização
```

## Requisitos

- Python 3.x
- Bibliotecas:
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `numpy`

Para instalar as dependências, execute:
```bash
pip install pandas scikit-learn matplotlib numpy
```

## Como Usar

### 1. Processar Tabelas de Genomas

1. **Prepare o Arquivo de Entrada**:
   - Substitua o caminho do arquivo `file_name` no script `process_genomes.py` para o caminho do seu arquivo `.tsv`.

2. **Execute o Script**:
   - Salve o script como `process_genomes.py`.
   - Execute no terminal:
     ```bash
     python process_genomes.py
     ```

3. **Arquivos Gerados**:
   - `tabela_original.csv`
   - `tabela_filtrada_complete_genome.csv`
   - `tabela_nao_redundante.csv`
   - `detailed_filtering.txt`

### 2. Clusterizar Genomas

1. **Certifique-se de que a Tabela Não Redundante está Disponível**:
   - Garanta que o arquivo `tabela_nao_redundante.csv` foi gerado.

2. **Execute o Script**:
   - Salve o script como `genome_clustering.py`.
   - Execute no terminal:
     ```bash
     python genome_clustering.py
     ```

3. **Saída Gerada**:
   - O gráfico será exibido e salvo como `clustering_plot.png` no diretório `Outputs`.

## Exemplos de Saída

### Relatório (`detailed_filtering.txt`)
```
Etapa 1: Arquivo original carregado com XX registros.
Etapa 2: Após filtrar apenas 'Complete Genome', restaram XX registros. Foram removidos XX registros.
Etapa 3: Após remover redundâncias, restaram XX registros. Foram removidos XX registros.
Média do 'Size' na tabela final (não redundante): XX.YY
```

### Gráfico de Clusterização (`clustering_plot.png`)

O gráfico de dispersão apresentará os clusters identificados, com cores diferentes para cada cluster, baseando-se no tamanho dos genomas.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
