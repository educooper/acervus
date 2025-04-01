from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)