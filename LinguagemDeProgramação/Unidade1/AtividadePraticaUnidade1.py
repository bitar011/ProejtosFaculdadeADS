#Função para cadastrar notas
def cadastrar_notas():
    notas = []
    while True:
        nota = float(input("Digite a nota do aluno (ou -1 para parar): "))
        if nota == -1:
            break
        notas.append(nota)
    return notas

#Função para calcular a média
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

#Função para verificar situação do aluno
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

#Função para exibir o relatório final
def exibir_relatorio(notas, media, situacao):
    print("\n=== RELATÓRIO FINAL ===")
    print(f"Notas inseridas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

#Programa principal
def main():
    print("Sistema de Gestão de Notas")
    notas = cadastrar_notas()
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    exibir_relatorio(notas, media, situacao)

#Executa o programa
main()
