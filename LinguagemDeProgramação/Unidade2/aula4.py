#Módulos e Bibliotecas:
#import math as m

#print(m.log2(1024))

#------------------------
#Matplotlib
#import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5]
#y = [2, 4, 1, 3, 5]

#plt.plot(x, y)

#plt.xlabel('Eixo X')
#plt.ylabel('Eixo Y')

#plt.title('Exemplo de gráfico de Linha')

#plt.show()

#------------------------------------------
#Prática geral:
import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [120, 90, 150, 80, 100]

plt.bar(meses, vendas, color='royalblue')

plt.xlabel('MESES')
plt.ylabel('Vendas (em Unidades)')

plt.title('Vendas Mensais')

plt.show()

#anotações gerais feitas em caderno.
#aula completa com mais informações com anotações