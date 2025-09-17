#Visualização de dados
#Matplotlib
#import matplotlib.pyplot as plt
#import random

#dados1 = random.sample(range(100), k=20)
#dados2 = random.sample(range(100), k=20)
#print(dados1)
#plt.bar(dados1, dados2)

#--------------------------
#Pandas
#import pandas as pd
#import matplotlib.pyplot as plt

#dados = {
#    'Produto': ['A', 'B', 'C'],
#    'qtde_vendida': [33, 50, 45]
#}

#df = pd.DataFrame(dados)
#df.plot(x='Produto', y='qtde_vendida', kind='bar')
#df.plot(x='Produto', y='qtde_vendida', kind='pie')
#df.plot(x='Produto', y='qtde_vendida', kind='line')
#plt.show()

#---------------------------------------------------
#Seaborn
#import seaborn as sns
#import matplotlib.pyplot as plt

#sns.set(style="whitegrid")

#df_tips = sns.load_dataset('tips')
#print(df_tips)

#fig, ax = plt.subplots(1, 3, figsize=(15, 5))

#sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
#sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
#sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)

#--------------------------------------------------------
#Aplicação geral
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

df = sns.load_dataset('tips')

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette="Set2")
plt.xlabel('Período(Time)')
plt.ylabel('Total de Gastos')
plt.title('Total de gastos por período(Almoço ou jantar)')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df)#, estimator=sum, ci=None, palette="Set2")
plt.xlabel('Período(Time)')
plt.ylabel('Média de Gastos')
plt.title('Média de gastos por período(Almoço ou jantar)')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, palette="Set3")
plt.xlabel('Período(Time)')
plt.ylabel('Média da Gorjeta')
plt.title('Média da Gorjeta por período(Almoço ou jantar)')
plt.show()

