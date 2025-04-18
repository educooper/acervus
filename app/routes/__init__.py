from .api.articles import api_articles

def register_routes(app):
    app.register_blueprint(api_articles)
