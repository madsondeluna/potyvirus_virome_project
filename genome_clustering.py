import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Carregar o arquivo no mesmo diretório do script
file_path = 'tabela_nao_redundante.csv'  # Certifique-se de que o arquivo está no mesmo diretório
data = pd.read_csv(file_path)

# Preparar os dados para clustering (utilizando o tamanho do genoma)
data_clustering = data[['Organism Scientific Name', 'Size']].dropna()

# Normalizar os tamanhos para o clustering
sizes = np.array(data_clustering['Size']).reshape(-1, 1)

# Aplicar o algoritmo K-means (escolher 4 clusters como exemplo)
kmeans = KMeans(n_clusters=4, random_state=42)
data_clustering['Cluster'] = kmeans.fit_predict(sizes)

# Mapear os clusters para cores
colors = ['blue', 'green', 'red', 'orange']
data_clustering['Color'] = data_clustering['Cluster'].map(lambda x: colors[x])

# Criar o gráfico de dispersão
plt.figure(figsize=(12, 8))
for cluster_id, color in enumerate(colors):
    cluster_data = data_clustering[data_clustering['Cluster'] == cluster_id]
    plt.scatter(cluster_data['Organism Scientific Name'], cluster_data['Size'],
                label=f'Cluster {cluster_id + 1}', color=color, alpha=0.7, edgecolor='k')

plt.xticks(rotation=90, fontsize=8)
plt.title('Clustering de Espécies por Tamanho do Genoma')
plt.xlabel('Espécie (Nome Científico)')
plt.ylabel('Tamanho do Genoma (bp)')
plt.legend()
plt.tight_layout()
plt.show()
