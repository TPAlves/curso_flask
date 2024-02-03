from flask import Blueprint, Response, request
from model.models import Disciplina, db
import json


app = Blueprint("disciplinas", __name__)


@app.route('/')
def index():
    disciplinas = Disciplina.query.all()
    result = [disciplina.to_dict() for disciplina in disciplinas]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = Disciplina.query.get(id)
    if row:
        return Response(response=json.dumps({'status': 'sucess', 'data': row.to_dict()}), status=200, content_type="application/json")
    return Response(response=json.dumps({'status': 'error', 'data': "not found"}), status=404, content_type="application/json")

@app.route('/add', methods=['POST'])
def add():
    disciplina = Disciplina(request.json['nome'])
    db.session.add(disciplina)
    db.session.commit()
    return Response(response=json.dumps({'status': 'sucess', 'data': disciplina.to_dict()}), status=201, content_type="application/json")

@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    disciplina = Disciplina.query.get(id)
    disciplina.nome = request.json['nome']
    db.session.commit()
    return Response(response=json.dumps({'status': 'sucess', 'data': disciplina.to_dict()}), status=200, content_type="application/json")


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    disciplina = Disciplina.query.get(id)
    db.session.delete(disciplina)
    db.session.commit()
    return Response(response=json.dumps({'status': 'sucess', 'data': disciplina.to_dict()}), status=200, content_type="application/json")
