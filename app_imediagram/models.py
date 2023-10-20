from app_imediagram import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from datetime import datetime
import pytz
from sqlalchemy import event



@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

    def obter_nome_usuario(self):
        # Consulte o usuário associado a esta foto
        if self.usuario:
            return self.usuario.username
        else:
            return "Usuário Desconhecido"

    def obter_hora_min_seg(self):
        hora_de_brasilia = self.data_criacao.astimezone(pytz.timezone('America/Sao_Paulo'))
        return self.data_criacao.strftime('%d-%m-%Y %H:%M:%S')