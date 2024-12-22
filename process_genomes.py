# Importar as bibliotecas necessárias
import pandas as pd

# Etapa 1: Carregar a tabela de um arquivo local
file_name = "data_summary.tsv"  # Substitua pelo nome do seu arquivo
data = pd.read_csv(file_name, sep="\t")

# Etapa 2: Salvar a tabela original
output_file_original = "tabela_original.csv"
data.to_csv(output_file_original, index=False)

# Armazenar o número de registros da tabela original
count_original = len(data)

# Exibir mensagem da etapa original
message_1 = f"Etapa 1: Arquivo original carregado com {count_original} registros."

# Etapa 3: Filtrar a tabela para manter apenas "Complete Genome" na coluna "Level"
data_filtered = data[data["Level"] == "Complete Genome"]
output_file_filtered = "tabela_filtrada_complete_genome.csv"
data_filtered.to_csv(output_file_filtered, index=False)

# Armazenar o número de registros da tabela filtrada
count_filtered = len(data_filtered)

# Exibir mensagem da etapa filtrada
message_2 = f"Etapa 2: Após filtrar apenas 'Complete Genome', restaram {count_filtered} registros. Foram removidos {count_original - count_filtered} registros."

# Etapa 4: Remover redundâncias com base na coluna "Organism Scientific Name"
# Manter apenas o registro com maior "Size" para cada espécie
data_non_redundant = data_filtered.loc[
    data_filtered.groupby("Organism Scientific Name")["Size"].idxmax()
]
output_file_non_redundant = "tabela_nao_redundante.csv"
data_non_redundant.to_csv(output_file_non_redundant, index=False)

# Armazenar o número de registros da tabela final
count_non_redundant = len(data_non_redundant)

# Calcular a média do "Size" da tabela final
mean_size = data_non_redundant["Size"].mean()

# Exibir mensagem da etapa final
message_3 = f"Etapa 3: Após remover redundâncias, restaram {count_non_redundant} registros. Foram removidos {count_filtered - count_non_redundant} registros."
message_4 = f"Média do 'Size' na tabela final (não redundante): {mean_size:.2f}"

# Salvar o texto detalhado no arquivo "detailed_filtering.txt"
detailed_text = f"{message_1}\n{message_2}\n{message_3}\n{message_4}"
with open("detailed_filtering.txt", "w") as file:
    file.write(detailed_text)

# Mensagem final
print("Os seguintes arquivos foram gerados:")
print(f"- {output_file_original}")
print(f"- {output_file_filtered}")
print(f"- {output_file_non_redundant}")
print(f"- detailed_filtering.txt")
