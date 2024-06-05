import pandas as pd
import matplotlib.pyplot as plt

pib = pd.read_csv('ibge-pib.csv', sep=';')

pib_sorteados = pib.sort_values('PIB (1000 R$)', ascending=[False])
pib_sorteados[['Município', 'PIB (1000 R$)']].head(11)

# Porcentagem do PIB dos primeiros 20 municípios com maior PIB em relação ao total do PIB dos 100 municípios
porcentagens = pib['Participação PIB Brasil (%)']
total = porcentagens.sum()
soma = porcentagens[:20].sum()
calculo = (100*soma)/total
print(f'A porcentagem do PIB dos primeiros 20 municípios com maior PIB em relação ao total do PIB dos 100 municípios apresentados é: {calculo:.0f}%')

# Tabela com o número de municípios por estado
municipios = pd.DataFrame()
municipios['Número de Municípios'] = pib.groupby('UF')['Município'].count()
municipios.T

# Tabela com o número de municípios por região
regiao = pd.DataFrame()
regiao = pib.groupby('Região')['Município'].count()
print(regiao)

# Apresente um novo gráfico ou nova figura ou nova tabela que você julgar interessante sobre os dados.
# Por exemplo, que revele a proporção desses 100 municípios em relação ao PIB total do Brasil
# (precisará usar a informação da coluna 'Participação PIB Brasil (%)
restante = 100 - calculo
valores = [restante, calculo]
legendas = ['Restante do PIB', 'PIB da tabela']

plt.pie(valores, labels=legendas, autopct='%.f%%', explode=[0.01] * len(valores))