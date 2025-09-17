#Captura de dados com Pandas
#import pandas as pd
#import requests
#from datetime import date #adicioonado para adicionar colounas
#from datetime import datetime as dt #"

#url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/10?formato=json"

#headers = {"User-Agent": "Mozilla/5.0"}
#response = requests.get(url, headers=headers)

#df_selic = pd.DataFrame(response.json())

#print(df_selic)
#adicionando colunas
#data_extracao = date.today()

#df_selic['data_extracao'] = data_extracao
#df_selic['responsavel'] = "Victor"

#print(df_selic.info())
#df_selic.head()

#Buscando informações
#df_selic.loc[0]

#-------------------------------------------
#Aplicação/Prática geral da aula
import pandas as pd

data = {
    'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
    'quantidade de itens comprados': [3, 1, 4, 3, 2],
    'tipo de item': ['Eletrônico', 'Vestuário', 'Alimento', 'Eletrônico', 'Alimento'],
    'receita total': [120, 80, 60, 120, 90]
}

df = pd.DataFrame(data)

df.drop_duplicates(keep='last', inplace=True)
print(df)

df['preco do item'] = df['receita total'] / df['quantidade de itens comprados']

itens_acima_de_50 = df[df['preco do item'] > 50]
print("Itens acima de 50 reais:")
print(itens_acima_de_50)