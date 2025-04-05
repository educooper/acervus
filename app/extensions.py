from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_session import Session
from authlib.integrations.flask_client import OAuth

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
session = Session() 
oauth = OAuth() 

# Define a view de login padrão (como estava no __init__)
login_manager.login_view = "register.login"
