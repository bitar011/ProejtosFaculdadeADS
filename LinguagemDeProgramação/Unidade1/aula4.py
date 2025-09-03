notas = [7.0, 6.5, 5.0]

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

arredondar_media = lambda media : round(media, 2)

media = calcular_media(notas)
medida_arredondada = arredondar_media(media)

situacao = "Aprovado" if medida_arredondada >= 6 else "Reprovado"

print("Notas do estudante: ", notas)
print("Média das notas: ", medida_arredondada)
print("Situação do estudante: ", situacao)