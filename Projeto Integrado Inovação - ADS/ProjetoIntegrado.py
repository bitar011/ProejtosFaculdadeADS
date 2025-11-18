#SISTEMA CLÍNICA VIDA+

#Lista para armazenar os dicionários de pacientes
pacientes = []

def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTE ---")
    nome = input("Nome do paciente: ")
    
    #Tratamento de erro para idade (deve ser número inteiro)
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("A idade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: Por favor, digite um número válido para a idade.")
            
    telefone = input("Telefone: ")
    
    #Armazenando em dicionário dentro da lista
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def exibir_estatisticas():
    print("\n--- ESTATÍSTICAS ---")
    if not pacientes:
        print("Nenhum paciente cadastrado para gerar estatísticas.")
        return

    total_pacientes = len(pacientes)
    soma_idades = sum(p["idade"] for p in pacientes)
    media_idade = soma_idades / total_pacientes
    
    #Encontrando mais novo e mais velho usando lambda
    paciente_mais_novo = min(pacientes, key=lambda x: x["idade"])
    paciente_mais_velho = max(pacientes, key=lambda x: x["idade"])

    print(f"Total de pacientes: {total_pacientes}")
    print(f"Média de idade: {media_idade:.1f} anos")
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")

def buscar_paciente():
    print("\n--- BUSCAR PACIENTE ---")
    nome_busca = input("Digite o nome para buscar: ").lower()
    encontrado = False
    
    for p in pacientes:
        if nome_busca in p["nome"].lower():
            print(f"Encontrado: Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
            encontrado = True
    
    if not encontrado:
        print("Paciente não encontrado.")

def listar_todos():
    print("\n--- LISTA GERAL ---")
    if not pacientes:
        print("Nenhum cadastro.")
    else:
        for i, p in enumerate(pacientes, 1):
            print(f"{i}. {p['nome']} - {p['idade']} anos - {p['telefone']}")

#Loop Principal (Menu)
while True:
    print("\n--- SISTEMA CLÍNICA VIDA+ ---")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        exibir_estatisticas()
    elif opcao == "3":
        buscar_paciente()
    elif opcao == "4":
        listar_todos()
    elif opcao == "5":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")