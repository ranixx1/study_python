import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados
df = pd.read_excel('pandas/Vendas.xlsx')

# Agrupa por loja e soma as quantidades
vendas_loja = df.groupby('ID Loja')['Quantidade'].sum().sort_values(ascending=False)

# Tamanho da figura
plt.figure(figsize=(12, 6))

# Gráfico de barras
vendas_loja.plot(kind='bar', color='skyblue', edgecolor='black')

# Títulos e rótulos
plt.title('Quantidade Total Vendida por Loja', fontsize=16)
plt.xlabel('ID da Loja', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibe o gráfico
plt.tight_layout()
plt.show()
