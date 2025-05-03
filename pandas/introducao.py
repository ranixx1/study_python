import pandas as pd
#dafaframes 
dados = {
    "Nome":["Ranilton","Lucas","Leonardo"],
    "Idade":[19,25,22],
}
df=pd.DataFrame(dados)
df

#series

s=pd.Series([10,20,30])
s

#lendo tabelas

di=pd.read_csv('planilha.csv')
di
#excel
diex=pd.read_excel('planilha.xlsx', sheet_name='nome')
diex

#manipulação basica de dados
df.head() #5 primeiras linhas
df.tail() #5 ultimas linhas

#colunas especificas
df[['Nome', 'Idade']]
df['Idade',]

#series booleanas e filtros
df['idade'>30] #serie booleana de true e false 
df[df['idade']>30] #retorna todos os funcionarios com idade maior que 30
df[df['Salario']>5000] #retorna todos os funcionarios com salario maior que 5000

#combinando filtros
filtro_maior_que30 = df['idade'>30]
filtro_mais_de_5mil = df['Salario'>5000]
df[filtro_maior_que30 & filtro_mais_de_5mil]

#criando 
df['Salario Anual'] = df['Salario']*12
df

#removendo colunas
df = df.drop('Salario Anual', axis=1)
df

#resumindo dados
df.info() #resumo infomtativo(tipo de dado e se tem null)
df.describe() #resumo esstatico
df['Salario'].sum() #soma de salario
df['Salario'].mean() # media de salario

#limpeza de dados
df.dropna()
