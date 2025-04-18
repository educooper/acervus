from flask import Blueprint, jsonify, request, abort
from app.models.articles import Article  # modelo de artigo
from app import db
from sqlalchemy import or_, and_
from datetime import datetime

api_articles = Blueprint('api_articles', __name__)

# GET /api/articles → Lista todos os artigos
@api_articles.route('/api/articles', methods=['GET'])
def list_articles():
    articles = Article.query.all()
    return jsonify([{
        'id': a.id,
        'title': a.title,
        'abstract': a.abstract,
        'author': a.author_name,
        'tags': [t.name for t in a.tags]
    } for a in articles]), 200


@api_articles.route('/api/articles/search', methods=['GET'])
def search_articles():
    q = request.args.get('q', '', type=str)
    tags = request.args.get('tags', '', type=str).split(',') if request.args.get('tags') else []
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = Article.query

    # Filtro por termo
    if q:
        query = query.filter(
            or_(
                Article.title.ilike(f'%{q}%'),
                Article.abstract.ilike(f'%{q}%'),
                Article.author_name.ilike(f'%{q}%')
            )
        )

    # Filtro por tags
    if tags:
        query = query.filter(Article.tags.any(Article.tags.property.mapper.class_.name.in_(tags)))

    # Filtro por datas
    if start_date:
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            query = query.filter(Article.created_at >= start)
        except ValueError:
            return jsonify({'error': 'Invalid start_date format. Use YYYY-MM-DD'}), 400

    if end_date:
        try:
            end = datetime.strptime(end_date, '%Y-%m-%d')
            query = query.filter(Article.created_at <= end)
        except ValueError:
            return jsonify({'error': 'Invalid end_date format. Use YYYY-MM-DD'}), 400

    results = query.all()

    return jsonify([
        {
            'id': a.id,
            'title': a.title,
            'abstract': a.abstract,
            'author': a.author_name,
            'tags': [t.name for t in a.tags],
            'created_at': a.created_at.isoformat() if a.created_at else None
        }
        for a in results
    ])


# GET /api/articles/<id> → Detalhe de um artigo
@api_articles.route('/api/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = Article.query.get_or_404(article_id)
    return jsonify({
        'id': article.id,
        'title': article.title,
        'abstract': article.abstract,
        'author': article.author_name,
        'tags': [t.name for t in article.tags]
    }), 200


# POST /api/articles → Criação de artigo
@api_articles.route('/api/articles', methods=['POST'])
def create_article():
    data = request.get_json()
    title = data.get('title')
    abstract = data.get('abstract')
    author_name = data.get('author')
    
    if not title or not author_name:
        return jsonify({'error': 'title and author are required'}), 400

    new_article = Article(title=title, abstract=abstract, author_name=author_name)
    db.session.add(new_article)
    db.session.commit()

    return jsonify({'message': 'Article created', 'id': new_article.id}), 201


# PUT /api/articles/<id> → Atualiza artigo
@api_articles.route('/api/articles/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    article = Article.query.get_or_404(article_id)
    data = request.get_json()

    article.title = data.get('title', article.title)
    article.abstract = data.get('abstract', article.abstract)
    article.author_name = data.get('author', article.author_name)

    db.session.commit()
    return jsonify({'message': 'Article updated'}), 200


# DELETE /api/articles/<id> → Remove artigo
@api_articles.route('/api/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({'message': 'Article deleted'}), 200
