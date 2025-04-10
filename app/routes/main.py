#main_bp = Blueprint('main', __name__)

#@main_bp.route('/')
#def index():
#    return "<h1>Bem-vindo ao Acervus 2.0!</h1>"

from app.models.articles import Article  # importa o modelo corretamente
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("home.html")

@main_bp.route("/acervus")
def acervus():
    return render_template("acervus.html")

@main_bp.route("/articles")
def artigos():
    artigos = Article.query.order_by(Article.created_at.desc()).all()
    return render_template("artigos.html", artigos=artigos)


@main_bp.route("/register")
def cadastro():
    return render_template("cadastro.html")

@main_bp.route("/dashboard")
def dashboard():
    return render_template("painel.html")

@main_bp.route("/sobre")
def sobre():
    return render_template("sobre.html")

@main_bp.route("/politicas-de-privacidade")
def politicas():
    return render_template("politicas.html")
