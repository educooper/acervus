#models/articles.py
from app.extensions import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(360), nullable=False)
    content = db.Column(db.Text) 
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Relacionamento com o usuário
    year = db.Column(db.Integer, nullable=False)
    file_url = db.Column(db.String(500))  # Link para o PDF armazenado
    status = db.Column(db.String(20), default="rascunho")  # ['rascunho', 'submetido', 'aprovado', 'rejeitado']
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship('User', back_populates='articles')
    tags = db.relationship('Tag', secondary='article_tags', back_populates='articles')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id,
            "year": self.year,
            "file_url": self.file_url,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "author": self.author.to_dict() if self.author else None,
            "tags": [tag.name for tag in self.tags]
        }
