from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_session import Session  # 🔹 Adicione esta linha!
from config import Config


# Configuração da aplicação via arquivo externo (opcional)
# app.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'config.py'))

# Criar a aplicação Flask
app = Flask(__name__)

app.config.from_object(Config)

app.config['SESSION_TYPE'] = 'filesystem'  # Garante que as sessões são armazenadas corretamente
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "register.login"
Session(app)  # Inicializa o Flask-Session

# Importando Blueprints
from app.routes.register import register_bp
from app.routes.auth import auth_bp
from app.routes.main import main_bp

app.register_blueprint(register_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
