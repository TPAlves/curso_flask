# Aula 13 - Upload de Arquivos
import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')

@app.route('/')
def index():
    print(UPLOAD_FOLDER)
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(filename=file.filename))
    file.save(savePath)
    return 'Upload feito com sucesso'

@app.route('/getfile/<filename>', methods=['GET'])
def getfile(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + '.jpeg')
    return send_file(file, mimetype="imagem/jpeg")

if __name__ == '__main__':
    app.run(debug=True)