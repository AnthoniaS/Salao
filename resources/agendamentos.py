from flask import Blueprint, jsonify, request
from banco import db
from models.modelAgendamento import Agendamento
from flask_jwt_extended import jwt_required

agendamentos = Blueprint('agendamentos', __name__)


@agendamentos.route('/agendamentos')

def cadastro():
    agendamentos = Agendamento.query.order_by(Agendamento.nome).all()
    return jsonify([agendamento.to_json() for agendamento in agendamentos])


@agendamentos.route('/agendamentos', methods=['POST'])
@jwt_required
def inclusao():
    agendamento = Agendamento.from_json(request.json)
    db.session.add(agendamento)
    db.session.commit()
    return jsonify(agendamento.to_json()), 201


@agendamentos.route('/agendamentos/<int:id>')

def consulta(id):
    agendamento = Agendamento.query.get_or_404(id)
    return jsonify(agendamento.to_json()), 200


@agendamentos.errorhandler(404)

def id_invalido(error):
    return jsonify({'id': 0, 'message': 'not found'}), 404


@agendamentos.route('/agendamentos/<int:id>', methods=['PUT'])

def alteracao(id):
    agendamento = Agendamento.query.get_or_404(id)
    agendamento.nome = request.json['nome']
    agendamento.sobrenome = request.json['sobrenome']
    agendamento.telefone = request.json['telefone']
    agendamento.data = request.json['data']
    agendamento.hora = request.json['hora']
    agendamento.servico = request.json['servico']

    db.session.add(agendamento)
    db.session.commit()
    return jsonify(agendamento.to_json()), 204


@agendamentos.route('/agendamentos/<int:id>', methods=['DELETE'])

def exclui(id):
    Agendamento.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Agendamento excluído com sucesso'}), 200


@agendamentos.route('/agendamentos/pesq/<palavra>')

def pesquisa(palavra):
    
    agendamentos = Agendamento.query.order_by(Agendamento.nome).filter(
        Agendamento.nome.like(f'%{palavra}%')).all()
    
    return jsonify([agendamento.to_json() for agendamento in agendamentos])
