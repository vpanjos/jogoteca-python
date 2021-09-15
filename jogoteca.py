from flask import Flask, render_template, request, redirect, session, flash,url_for

app = Flask(__name__)
app.secret_key = 'alura'  # criar uma string de senha secreta para a sessao


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self,id, nome , senha):
        self.id = id
        self.nome = nome
        self.senha = senha

usuario1 = Usuario('fulano', 'Fulano da Silva', '1234')
usuario2 = Usuario('fulana', 'Fulana Pereira', '567')
usuario3 = Usuario('vanessa', 'Vanessa Anjos', 'vpa')

# dicionario de usuários
usuarios = { usuario1.id: usuario1,
             usuario2.id: usuario2,
             usuario3.id: usuario3}

# lista global desse pacote/arquivo
jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Call of Duty', 'Tiro', 'PS')
lista = [jogo1, jogo2, jogo3]


# Running http://127.0.0.1:5000/
@app.route('/')
def index():
    # lista = ['Tetris', 'Super Mario', 'Pokemon Gold'] - lista local
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


app.run(debug=True)
# app.run()
# parametro para a aplicacao restart apos salvar alteracao no codigo
