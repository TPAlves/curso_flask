# Aula 08 - Redirecionamentos e Erros 
from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'adm' and request.form['senha'] == 'adm':
            return redirect(url_for('sucesso'), code=302)
        return abort(401)
    
    return abort(403)

@app.route('/sucesso')
def sucesso():
    return 'sucesso'

if __name__ == '__main__':
    app.run(debug=True)
