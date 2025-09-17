#Introdução a biblioteca Pandas
#import pandas as pd

#exemplo1 = [10, 20, 30, 40, 50]

#series1 = pd.Series(data = exemplo1)

#print(series1)

#-------------------------------------
#Criando uma Serie a partir de um Dicionário
#import pandas as pd

#Exmplo2 = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E':500}

#series2 = pd.Series(data = Exmplo2)

#print(series2)

#--------------------------------------------
#Leitura de dados com Pandas
#import pandas as pd
#url = 'https://www.fdic.gov/bank-failures/failed-bank-list'
#dfs =  pd.read_html(url)

#print(type(dfs))
#print(len(dfs))

#df_bancos = dfs[0]
#print(df_bancos.shape)
#print(df_bancos.dtypes)

#df_bancos.head()

#----------------------------------------------
#Prática/aplicação geral da aula
import pandas as pd

dados = {
    'Nome': ['Victor', 'Gustavo', 'William', 'Rafael', 'Kauã'],
    'Idade': [19, 21, 21, 20, 21]
}

serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

print("Serie de Idades:")
print(serie_idades)

media_idades = serie_idades.mean()
print("\nMédia de Idades:", media_idades)