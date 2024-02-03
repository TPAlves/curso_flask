# Aula 15 - REST API parte 1

from flask import Flask, render_template, request, url_for, redirect, Response
from models import db, Estudante
import json 


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

@app.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [estudante.to_dict() for estudante in estudantes]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = Estudante.query.get(id)
    if row:
        return Response(response=json.dumps({'status': 'sucess', 'data': row.to_dict()}), status=200, content_type="application/json")
    return Response(response=json.dumps({'status': 'error', 'data': "not found"}), status=404, content_type="application/json")

@app.route('/add', methods=['POST'])
def add():
    estudante = Estudante(request.json['nome'], request.json['idade'])
    db.session.add(estudante)
    db.session.commit()
    return Response(response=json.dumps({'status': 'sucess', 'data': estudante.to_dict()}), status=201, content_type="application/json")

@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.json['nome']
    estudante.idade = request.json['idade']
    db.session.commit()
    return Response(response=json.dumps({'status': 'sucess', 'data': estudante.to_dict()}), status=200, content_type="application/json")


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps({'status': 'sucess', 'data': estudante.to_dict()}), status=200, content_type="application/json")


if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.debug = True    
    app.run()
