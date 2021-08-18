from flask import Flask, render_template, request

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# lista global desse pacote/arquivo
jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Call of Duty','Tiro','PS')
lista = [jogo1, jogo2,jogo3]

@app.route('/')
def index():
    # lista = ['Tetris', 'Super Mario', 'Pokemon Gold'] - lista local

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return  render_template('novo.html',titulo='Novo jogo')

@app.route('/criar',methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    # retornar a lista com o novo jogo
    return render_template('lista.html',
                           titulos='Jogos',
                           jogos=lista)

#app.run()

# parametro para a aplicacao restart apos salvar alteracao no codigo
app.run(debug=True)
