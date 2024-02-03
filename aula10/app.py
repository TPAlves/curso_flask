# Aula 10 - Enviando dados par ao template
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')

@app.route('/')
def notas():
    return render_template('notas.html')

@app.route('/calculo', methods=['GET', 'POST'])
def calculo():
    total = sum([int(i) for i in request.form.to_dict().values()])
    return render_template('resultado.html', total=total)
if __name__ == '__main__':
    app.run(debug=True)