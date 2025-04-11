# routes/articles.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.forms.article_form import ArticleForm
from app.models.articles import Article
from app.models.tags import Tag
from app.extensions import db
from flask_login import current_user, login_required
import os
from werkzeug.utils import secure_filename
from app.utils.pdf_utils import extract_text_from_pdf

articles_bp = Blueprint('articles', __name__)

UPLOAD_FOLDER = 'app/static/uploads'

@articles_bp.route('/articles/novo', methods=['GET', 'POST'])

@login_required
def novo_artigo():
    form = ArticleForm()
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.all()]

    if form.validate_on_submit():
        filename = None
        content = None
        if form.file.data:
            filename = secure_filename(form.file.data.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            form.file.data.save(filepath)

            # Extrair texto do PDF:
            content = extract_text_from_pdf(filepath)

        artigo = Article(
            title=form.title.data,
            year=form.year.data,
            file_url=f"/static/uploads/{filename}" if filename else None,
            content=content,
            author_id=current_user.id,
            tags=[Tag.query.get(tag_id) for tag_id in form.tags.data]
        )

        db.session.add(artigo)
        db.session.commit()
        flash('Artigo cadastrado com sucesso com indexação!')
        return redirect(url_for('main.dashboard'))

    return render_template('artigos/novo.html', form=form)


@articles_bp.route('/articles/editar/<int:artigo_id>', methods=['GET', 'POST'], endpoint='editar_artigo')
@login_required
def editar_artigo(artigo_id):
    artigo = Article.query.get_or_404(artigo_id)

    if artigo.user_id != current_user.id:
        flash('Você não tem permissão para editar este artigo.', 'danger')
        return redirect(url_for('main.dashboard'))

    form = ArticleForm(obj=artigo)

    if form.validate_on_submit():
        artigo.title = form.title.data
        artigo.content = form.content.data
        db.session.commit()
        flash('Artigo atualizado com sucesso!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('artigos/editar.html', form=form, artigo=artigo)
