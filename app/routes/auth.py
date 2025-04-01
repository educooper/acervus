from flask import Blueprint, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from app import app, db
from app.models.user import User
from flask_login import login_user

auth_bp = Blueprint('auth', __name__)
oauth = OAuth(app)

# Configuração do Google OAuth
oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params={'scope': 'openid email profile'},
    access_token_url='https://oauth2.googleapis.com/token',
    access_token_params=None,
    jwks_uri='https://www.googleapis.com/oauth2/v3/certs',  # 🔹 Adicione esta linha!
    client_kwargs={'scope': 'openid email profile'}
)

# Rota para iniciar login com Google
@auth_bp.route('/login/google')
def login_google():
    return oauth.google.authorize_redirect(url_for('auth.authorized', _external=True))

# Callback do Google após autenticação

@auth_bp.route('/login/authorized')
def authorized():
    try:
        print("Tentando obter o token OAuth...")
        token = oauth.google.authorize_access_token()
        print("Token recebido:", token)
    except Exception as e:
        print("Erro ao obter token:", e)
        return "Erro ao autenticar com o Google", 500


#@auth_bp.route('/login/authorized')
#def authorized():
#    token = oauth.google.authorize_access_token()
#    if token is None:
#        return 'Acesso negado!', 403

    session['google_token'] = token
    user_info = oauth.google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()

    # Verifica se o usuário já existe
    email = user_info.get('email')
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(name=user_info.get('name'), email=email, password_hash='')
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for('main.index'))
