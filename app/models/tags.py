#models/tags.py
from app.extensions import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    articles = db.relationship('Article', secondary='article_tags', back_populates='tags')

class ArticleTags(db.Model):
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
