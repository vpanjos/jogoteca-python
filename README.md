# Web app com Flask 
# Flask parte 1: Crie uma webapp com Python 3
# Notas
# pegaria a 0.11.1 que é última versão compatível com a 0.11.0
> pip3 install flask~=0.11.0 

==: versão exata - define uma versão fixa que deve ser instalada (como vimos no vídeo).
>!=: exclusão de versão - define a versão que não é para instalar, pegando assim a mais atual sem ser a definida.
<=, >=: versão maior ou igual e menor ou igual - ajuda a restringir versões, inclusive a definida.
<, >: versão maior ou menor - ajuda a restringir versões, excluindo a definida.

# Aula 1 - Listando jogos usando flask
> - Como adicionar conteúdos dinâmicos 
> - Como pegar dados do servidor 
> - Como mostrar os atributos na view

### parte 1
# Como definir uma rota
```python
app= Flask(__name__)
@app.route('/inicio') 
```

# Como usar templates HTML
```python
def ola():
 # retornando HTML estatico dentro do codigo python
return '<h1> Ola Flask!</h1>'
# Ou
 return render_template('lista.html')  # Usando pagina html renderizada
```
# Como rodar uma aplicação Flask
```python
# metodo padrao
app.run()

# trecho da app para definir host e porta
 app.run(host='0.0.0.0', port=8080)
```

# Jinja2
> Dentre as várias libs utilizadas pelo Flask, temos a chamada Jinja2, responsável por fazer com que a engine de templates funcione. Ou seja, permite renderizar conteúdo dinâmico em uma página HTML.
 
 # Aula 2 
-  Como adicionar conteúdos dinâmicos no HTML
```html
            <h1>{{ titulo }}</h1>
```
-    Como pegar dados do servidor
```html
 <tbody>
                {% for jogo in jogos %}
                    <tr>
                        <td>{{ jogo }}</td>
                    </tr>
                {% endfor %}
```
```python
    def ola():
    lista = ['Tetris', 'Super Mario', 'Pokemon Gold']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

```
 -   Como mostrar os atributos na view
```html
 <td>{{ jogo.nome }}</td>
                        <td>{{ jogo.categoria }}</td>
                        <td>{{ jogo.console }}</td>
```
# Aula 3 - Criando um jogo novo
- Como criar itens para nossa aplicação
  - Criar classe e passar os objetos na lista
  - Receber os atributos dos objetos no html 
- Como montar formulários utilizando o Flask 
- O que é e como resolver POSTs no servidor

# Aula 4 - Melhorando código e usabilidade
- Como criar templates
- Utilizando css
    - Incluir bootstrap:
    * Estático
    ```html
        <link rel="stylesheet" href="../static/bootstrap.css">
    ```
    * Url Dinâmica:
  
## Sessão - Login 
- session recebe um dicionario - criar um item,
- salvar o usuario que esta logado na sessao.
- Salvar o nome do usuario
- Importar o objeto session na aplicação e incluir uma nova chave neste objeto, que é um dicionário.
```python
def autenticar():
    if 'mestra' == request.form['senha']:
        
        session ['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')
```

# Aula 5
- Como criar a tela de login
- Como guardar os dados da sessão 
- Como deslogar a sessão

# Aula 6 
Implementando autorização para criação de jogos pelos usuários

##  Protegendo uma rota

## URls mais dinâmicas
- Usar função: 
  ```python 
  url_for('nome_método')
  ```
- Utilidade: Se uma rota for alterada eu continuo dependendo do nome da função ao invés da string da rota. Desta forma não é necessário alterar nada.
url_for passando o nome do método da rota, assim sempre irá pegar a rota retornada na função.
  
## Múltiplos usuários
- Criação de um dicionário de usuários com username e senha
- Comparar se o usuário enviado no form tem no dicionário de de usuários
```python
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario_logado = usuarios[request.form['usuario']]
        if usuario_logado.senha == request.form['senha']:
            session['usuario_logado'] = usuario_logado.id
        flash(usuario_logado.nome + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
```