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