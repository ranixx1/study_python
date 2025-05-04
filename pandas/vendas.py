import pandas as pd


#importando de uma planilha
vendas_df = pd.read_excel("pandas/Vendas.xlsx")

#pegar uma linha especifica
vendas_df.loc[1]

#pegar de varias linhas
vendas_df.loc[1:3]

#pegar linhas que correspondem a uma condição
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']
print(vendas_norteshopping_df)

#pegar varias linhas e colunas usando o loc
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping',['ID Loja', 'Produto', 'Quantidade']]
print(vendas_norteshopping_df)

#pegar um valor especifico
print(vendas_df.loc[1,'Produto'])
#adicionar uma coluna
#1-a partir de uma coluna que existe 
vendas_df['Comissão'] = vendas_df['Valor Final']*0.05
print(vendas_df)

#2-criar uma coluna padrão
vendas_df.loc[:, 'Imposto']=0

#adicionar uma linha
#vendas_df=vendas_df.append()

#excluir linha
vendas_df=vendas_df.drop('Imposto', axis=1) #eixo 0 é a linha e eixo 1 é a coluna

#tratar valores vazios
#deletar linhas e colunas completamente vazia
vendas_df = vendas_df.dropna(how='all') #linhas
vendas_df = vendas_df.dropna(how='all', axis=1) #colunas

#deletar linhas que possuem pelo menos 1 valor vazio
vendas_df = vendas_df.dropna()

#preencher valores vazios

#1-preencher com a media da coluna
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'.mean()])
print(vendas_df)

#2-preencher com o ultimo valor
vendas_df = vendas_df.ffill()

#calcular os indicadores
#value counts
transacoes_loja = vendas_df['ID Loja'].value_counts()
print(transacoes_loja)
#group by
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()

#mesclar 2 dataframes
#vendas_df = vendas_df.merge(tabela nova)

