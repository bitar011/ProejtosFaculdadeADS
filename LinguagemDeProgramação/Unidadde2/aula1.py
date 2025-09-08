#Listas:
#cores = ['vermelho', 'azul', 'amarelo', 'verde', 'roxo',]
#for cor in cores:
#    print(f'Posição = {cores.index(cor)}, cor = {cor}')

#Listcomp:
#linguagens = ["Python", "Java", "JavaScript", "C", "C#", "Go", "Kotlin", "Swift", "Ruby"]
#print("Antes da listcomp = ", linguagens)
#linguagens = [item.lower() for item in linguagens]
#print("\nDepois da listcomp = ", linguagens)

#Map:
#precos_em_dolar = [100, 50, 75, 120]
#taxa_de_cambio = 5.25
#precos_em_reais = list(map(lambda x: x*taxa_de_cambio, precos_em_dolar))
#print(precos_em_reais)

#Filter:
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
#print(numeros_pares)

#Tuplas:
#vogais = ('a', 'e', 'i', 'o', 'u')
#print(f"Tipo do objeto vogais = {type(vogais)}")
#for p, x in enumerate(vogais):
#    print(f"Posição = {p}, valor= {x}")

#Prática geral:
convidados = ("Gustavo", "Yasmin", "Lara", "Thaylla", "William", "Kauã", "Ingrid")
confirmados = ["Gustavo", "Yasmin", "Thaylla"]
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
print("Convidados que ainda não confirmaram:")
for pessoa in nao_confirmados:
    print(pessoa)
print("\nEnviando lembrete para os convidados que ainda não confirmaram.")