from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    print("Tabelas detectadas:")
    print(db.metadata.tables.keys())
