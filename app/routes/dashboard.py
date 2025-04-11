from flask import Blueprint, render_template
from app.models.articles import Article

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])

def dashboard():
    form = painelForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(name=form.name.data, email=form.email.data, password_hash=hashed_password)
        artigos = Article.query.filter_by(user_id=current_user.id).order_by(Article.created_at.desc()).all()
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('painel.html', form=form)