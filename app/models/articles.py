from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    tags = db.Column(db.String(255))
    file_url = db.Column(db.String(500))  # Link para o PDF armazenado
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
