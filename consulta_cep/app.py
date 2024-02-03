from flask import Flask, redirect, render_template, url_for, request
import requests, json

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sucesso/<cep>')
def sucesso(cep):
    request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    conversao = json.loads(request.content)
    print(conversao)
    return (f'Cep: {conversao}')


@app.route('/buscacep', methods=['POST', 'GET'])
def buscacep():
    if request.method == 'POST':
        dado = request.form['cep']
        return redirect(url_for('sucesso', cep=dado))
    else:
        dado = request.args.get('cep')
        return redirect(url_for('sucesso', cep=dado))


if __name__ == '__main__':
    app.run()

