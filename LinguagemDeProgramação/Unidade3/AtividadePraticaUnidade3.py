import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# Passo 1: Conectar ao banco
# --------------------------
conexao = sqlite3.connect("dados_vendas.db")
cursor = conexao.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
""")

# --------------------------
# Passo 2: Inserir dados (usuário informa)
# --------------------------
print("Cadastro de vendas")
while True:
    data = input("Digite a data da venda (AAAA-MM-DD): ")
    produto = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria: ")
    valor = float(input("Digite o valor da venda: "))

    cursor.execute("INSERT INTO vendas (data_venda, produto, categoria, valor_venda) VALUES (?, ?, ?, ?)",
                   (data, produto, categoria, valor))
    conexao.commit()

    opc = input("Deseja cadastrar outra venda? (s/n): ")
    if opc.lower() != "s":
        break

# --------------------------
# Passo 3: Carregar dados no Pandas
# --------------------------
df = pd.read_sql_query("SELECT * FROM vendas", conexao)
print("\n📊 Dados de vendas cadastrados:")
print(df)

# --------------------------
# Passo 4: Análise dos dados
# --------------------------
print("\nAnálises:")
print("Total de vendas:", df["valor_venda"].sum())
print("Média de vendas:", df["valor_venda"].mean())
print("Vendas por categoria:\n", df.groupby("categoria")["valor_venda"].sum())

# --------------------------
# Passo 5: Visualizações
# --------------------------
# Gráfico de barras por categoria
plt.figure(figsize=(6,4))
sns.barplot(data=df, x="categoria", y="valor_venda", estimator=sum)
plt.title("Total de vendas por categoria")
plt.show()

# Gráfico de linha ao longo do tempo
df["data_venda"] = pd.to_datetime(df["data_venda"])
df_por_data = df.groupby("data_venda")["valor_venda"].sum().reset_index()

plt.figure(figsize=(8,4))
sns.lineplot(data=df_por_data, x="data_venda", y="valor_venda", marker="o")
plt.title("Evolução das vendas ao longo do tempo")
plt.xticks(rotation=45)
plt.show()

conexao.close()
