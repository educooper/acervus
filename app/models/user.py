from app.extensions import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash
from app.extensions import db  # ou o caminho do seu db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    codigo_recuperacao = db.Column(db.String(6), nullable=True)
    phone = db.Column(db.String(20), nullable=True)  # certifique-se de que esse campo está lá

    #Adicione essa linha aqui
    
    articles = db.relationship("Article", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.email}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
