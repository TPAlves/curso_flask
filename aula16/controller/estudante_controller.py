from flask import Blueprint, Response, request
from model.models import Estudante, db
import json


app = Blueprint("estudantes", __name__)


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
