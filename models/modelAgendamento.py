from banco import db
import hashlib
from config import config

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    sobrenome = db.Column(db.String(60), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Integer, nullable=False)
    hora = db.Column(db.Integer, nullable=False)
    servico = db.Column(db.String(60), nullable=False)
    

    def to_json(self):
        json_agendamentos = {
            'id': self.id,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'telefone': self.telefone,
            'data': self.data,
            'hora': self.hora,
            'servico': self.servico
            
        }
        return json_agendamentos

    @staticmethod
    def from_json(json_agendamentos):
        nome = json_agendamentos.get('nome')
        sobrenome = json_agendamentos.get('sobrenome')
        telefone = json_agendamentos.get('telefone')
        data = json_agendamentos.get('data')
        hora = json_agendamentos.get('hora')
        servico = json_agendamentos.get('servico')

        return Agendamento(nome=nome, sobrenome=sobrenome, telefone=telefone, data=data, hora=hora, servico=servico)
