#Exemplo de Front-end com Python
#html_code = """
#<!DOCTYPE html>
#<html>
#<head>
#    <tittle>Exemplo de Front-end com Python</tittle>
#</head>
#<body>
#    <h1>Olá, Mundo!</h1>
#    <p>Essa é uma página web, criada no VSCode</p>
#</body>
#</html>
#"""

# Cria um arquivo HTML
#with open("pagina.html", "w", encoding="utf-8") as file:
#    file.write(html_code)

#print("Arquivo 'pagina.html' criado com sucesso!")

#--------------------------------------------------
#Exemplo de Back-end web com Python
#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello():
#   return 'Bem vindo ao Back-end simples com Flask'

#if __name__ == '__main__':
#    app.run(host='localhost', port=5000)

#---------------------------------------------------
#Aplicação Geral
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplicação Aula 1</title>
</head>
<body style="border: none; padding: 0; font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; box-sizing: border-box;">
    <header style="background-color: cadetblue; text-align: center; padding: 20px;">
        <h1 style="margin: 0;">Victor Bitar</h1>
        <p style="margin: 5px 0;">Desenvolvedor Web</p>
    </header>

    <section style="margin: 20px; text-align: center;">
        <img src="" alt="Sua Foto" style="border-radius: 50%; margin-bottom: 20px;">
        <div id="info-pessoais" style="max-width: 400px; margin: 0 auto;">
            <p>Cidade: Jequié</p>
            <p>País: Brasil</p>
            <p>Interesses: Back-end Developmant, Programação, etc.</p>
        </div>
    </section>

    <section style="margin: 20px; text-align: center;">
        <h2>Habilidades</h2>
        <ul style="list-style: none; padding: 0;">
            <li>Limguagens: Python, Java, HTML, CSS, JavaScrit</li>
            <li>Ferramentas: Git, VSCode</li>
        </ul>
    </section>

    <section style="margin: 20ppx; text-align: center;">
        <h2>Projeto Recente</h2>
        <p>Trabalhando em um projeto pessoal para mostrar meu  portifólio</p>
    </section>

    <footer style="text-align: center; margin-top: 20px;">
        <a href="http://www.linkedin.com/in/victor-bitarv" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;"></a>
    </footer>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_code)