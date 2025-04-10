from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager, session, oauth
from app.routes.auth import auth_bp, configure_google_oauth
from app.models.user import User
from app.models.articles import Article
from app.models.tags import Tag, ArticleTags
from app.models.password_reset_code import PasswordResetCode
from flask_login import LoginManager
from app.models import * 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    session.init_app(app)
    oauth.init_app(app) 

    login_manager.login_view = "register.login"

    from app.routes.register import register_bp
    from app.routes.login import login_bp
    from app.routes.auth import auth_bp, configure_google_oauth
    from app.routes.main import main_bp

    app.register_blueprint(register_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(login_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        from app.models.user import User
        db.create_all()
        configure_google_oauth()


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
