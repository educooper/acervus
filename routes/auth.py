from flask import Blueprint, redirect, url_for, session
from flask_oauthlib.client import OAuth
from acervus import acervus, db
from acervus.models.user import User
from flask_login import login_user

auth_bp = Blueprint('auth', __name__)
oauth = OAuth(acervus)

# Configuração da aplicação via arquivo externo (opcional)
acervus.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'config.py'))

# Configuração do Google OAuth
google = oauth.remote_acervus(
    'google',
    consumer_key=f'{GOOGLE_CLIENT_ID}',
    consumer_secret=f'{GOOGLE_CLIENT_SECRET}',
    request_token_params={'scope': 'email'},
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth'
)

# Rota para iniciar login com Google
@auth_bp.route('/login/google')
def login_google():
    return google.authorize(callback=url_for('auth.authorized', _external=True))

# Callback do Google após autenticação
@auth_bp.route('/login/authorized')
def authorized():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Acesso negado!', 403

    session['google_token'] = response['access_token']
    user_info = google.get('userinfo')

    # Verifica se o usuário já existe
    email = user_info.data['email']
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(name=user_info.data['name'], email=email, password_hash='')
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for('dashboard'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')
