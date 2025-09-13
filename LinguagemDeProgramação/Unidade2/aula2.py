#SET:
#meu_conjunto = set()

#meu_conjunto.add(10)
#meu_conjunto.add(20)
#meu_conjunto.add(30)
#print("Conjuto após adicionar elementos: ", meu_conjunto)

#elemento = 20
#if elemento in meu_conjunto:
#    print(f"{elemento} está no conjunto.")
#else:
#    print(f"{elemento} não está no conjunto.")

#meu_conjunto.remove(20)
#print(f"conjunto após remover {elemento} do conjunto: {meu_conjunto}")

#---------------------------------------------------------------------------
#MAPPING:
#dici_1 = {}
#dici_1['nome'] = "Victor"
#dici_1['idade'] = 19

#dici_2 = {'nome': "Victor", 'idade': 19}
#dici_3 = dict([('nome', "Victor"), ('idade', 19)])
#dici_4 = dict(zip(['nome', 'idade'], ["Victor", 19]))

#print(dici_1 == dici_2 == dici_3 == dici_4)
#print(dici_1)

#------------------------------------------------------
#ARRAY NUMPY
#import numpy as np

#my_array = np.array([1, 2, 3, 4, 5])
#print("Array original:")
#print(my_array)

#squared_arrey = my_array ** 2
#sum_of_elements = np.sum(my_array)

#print("\nArray ao quadrado:")
#print(squared_arrey)
#print("\nSoma de todos elementos:")
#print(sum_of_elements)

#elements_at_index_2 = my_array[2]
#print(f"\nElemento no índice 2: {elements_at_index_2}")

#-----------------------------------------------------------
#PRÁTICA GERAL:
import numpy as np

participantes = [
    {
        "nome": "Victor",
        "localização": "Brasil",
        "afiliação": "Faculdade Anhanguera",
        "interesses": ["T.I", "Programação"]
    },
    {
        "nome": "Gusttavo",
        "localização": "França",
        "afiliação": "Faculdade Unex",
        "interesses": ["Poesia", "Psicologia"]
    },
    {
        "nome": "William",
        "localização": "Arábia",
        "afiliação": "Faculdade Unex",
        "interesses": ["T.I", "Basquete"]
    }
]    

regiões = set(participante["localização"] for participante in participantes)
afiliacoes = {}

for participante in participantes:
    afiliacao = participante["afiliação"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

print(f"Regiões dos participantes: {regiões}")
print("Afiliação dos participantes:")
for afiliacao, nomes in afiliacoes.items():
    print(f"{afiliacao}: {', '.join(nomes)}")
print(f"Area de interesse mais popular: {area_mais_popular}")