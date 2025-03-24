from flask import Flask
from acervus import Acervus
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

acervus = Flask(__name__)

db = SQLAlchemy(acervus)


if __name__ == '__main__':
    db.create_all()
    acervus.run(debug=True)