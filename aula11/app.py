# Aula 11 - Cookies
from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET','POST'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))

    if request.method == 'POST':
        data = request.form['cookie']
        resp.set_cookie('cookieData', data)
    
    return resp


@app.route('/getcookie')
def getcookie():
    cookieData = request.cookies.get('cookieData')
    return f'<h1>O valor é: {cookieData} </h1>'

if __name__ == '__main__':
    app.run(debug=True)
