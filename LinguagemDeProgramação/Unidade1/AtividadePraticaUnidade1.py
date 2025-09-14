#Sistema de Gestão de Notas
#Atividade Prática - Unidade 1
#Autor: Victor Bitar

#Função para cadastrar as notas
def cadastrar_notas():
    notas = []
    while True:
        nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
        if nota == -1: #condição de parada
            break
        notas.append(nota) #adiciona a nota na lista
    return notas

#Função para calcular a média das notas
def calcular_media(notas):
    if len(notas) == 0: #evita divisão por zero
        return 0
    media = sum(notas) / len(notas)
    return media

#Função para verificar se o aluno está aprovado ou reprovado
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

#Função para exibir o relatório final
def exibir_relatorio(notas, media, situacao):
    print("\n=== RELATÓRIO FINAL ===")
    print("Notas inseridas:", notas)
    print("Média:", round(media, 2))
    print("Situação:", situacao)

#Programa principal
def main():
    print("===== Sistema de Gestão de Notas =====")
    notas = cadastrar_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    exibir_relatorio(notas, media, situacao)

#Executa o programa
main()
