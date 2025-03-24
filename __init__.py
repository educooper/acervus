from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Criar a aplicação Flask
acervus = Flask(__name__)

# Configuração da aplicação via arquivo externo (opcional)
acervus.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'config.py'))

# Inicializar banco de dados e login
db = SQLAlchemy(acervus)
login_manager = LoginManager(acervus)
login_manager.login_view = "register.login"

@login_manager.user_loader
def load_user(user_id):
    from acervus.models.user import User
    return User.query.get(int(user_id))

# Importar e registrar os Blueprints
from acervus.routes.register import register_bp
from acervus.routes.auth import auth_bp

acervus.register_blueprint(register_bp, url_prefix='/')
acervus.register_blueprint(auth_bp, url_prefix='/auth')
