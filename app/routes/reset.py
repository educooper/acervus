# routes/reset.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.user import User
from app.forms.reset_password import ResetPasswordForm
from app import db
from app.utils.token import verify_reset_token
from werkzeug.security import generate_password_hash

reset_bp = Blueprint('reset', __name__)

@reset_bp.route('/reset/<token>', methods=['GET', 'POST'])
def reset_token(token):
    email = verify_reset_token(token)
    if not email:
        flash('Token inválido ou expirado.', 'danger')
        return redirect(url_for('login.login'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        user.password_hash = generate_password_hash(form.password.data)
        db.session.commit()
        flash('Senha atualizada com sucesso!', 'success')
        return redirect(url_for('login.login'))
    
    return render_template('reset_password.html', form=form)
