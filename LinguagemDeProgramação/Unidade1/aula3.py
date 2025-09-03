filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

print("Bem-Vindo a classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar. /n")

for filme in filmes:
    classificacao = input(f"Como você classificaria '{filme}' de 1 a 5?(ou 0 para sair)")

    if classificacao == '0':
        print("Que pena que não irá mais classificar.")
        break

    classificacao = int(classificacao)
    if classificacao < 1 or classificacao > 5:
        print("Por favor, digite uma nota válida de 1 a 5.")
    else:
        print(f"Você classificou '{filme}' com '{classificacao}' estrelas./n")
print("Obrigado por classificar os filmes!")