from app.routes.api.articles import api_articles  # importa o blueprint da API de artigos

def register_routes(app):
    # Aqui você registra todos os blueprints que são da API ou que quer centralizar
    app.register_blueprint(api_articles, url_prefix='/api')