from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return "<h1>Bem-vindo ao Acervus 2.0!</h1>"
