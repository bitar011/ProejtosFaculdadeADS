import sqlite3 

#conn = sqlite3.connect('exemplo.db')

#cursor = conn.cursor()

#create_teable = """
#CREATE TABLE IF NOT EXISTS Produtos(
#    id INTEGER PRIMARY KEY,
#    nome TEXT NOT NULL,
#    preco REALNOT NULL,
#    estoque INTEGER
#);
#"""

#cursor.execute(create_teable)

#novo_produto = ('Camiseta', 19.99, 50)
#inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

#cursor.execute(inserir_produto, novo_produto)
#conn.commit()

#selecionar_produtos = "SELECT * FROM Produtos"
#cursor.execute(selecionar_produtos)

#produtos = cursor.fetchall()
#for produto in produtos:
#    print(produto)

#conn.close()

#---------------------------------------------
#Prática aula geral(import mantido)
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT
    )
''')
dados_exemplo = [
    ('João', 'joao@email.com', '123-456-7890'),
    ('Maria', 'maria@emial.com', '987-654-3210'),
    ('Carlos', 'carlos@email.com', '555-777-8889')
]
cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)', dados_exemplo)
conn.commit()

cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print("Contatos:")
for contato in contatos:
    print(contato)

novo_telefone = '999-222-1133'
contato_id = 2
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()


conn.close()