from flask import Flask
from config import config
from banco import db
from resources.usuarios import usuarios
from resources.agendamentos import agendamentos
from flask_jwt_extended import JWTManager
from blacklist import blacklist

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(usuarios)
app.register_blueprint(agendamentos)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

@app.route('/')
def raiz():
    db.create_all()
    return '<h2>Beauty Space</h2>'


if __name__ == '__main__':
    app.run(debug=True)
