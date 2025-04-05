from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from flask_login import login_user
from app import db
from app.models.user import User
from app.forms.register import RegisterForm
from sqlalchemy.exc import IntegrityError 

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(name=form.name.data, email=form.email.data, password_hash=hashed_password)

        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('main.dashboard'))

        except IntegrityError:
            db.session.rollback()
            flash('Este email já está cadastrado. Tente outro.', 'danger')

    return render_template('cadastro.html', form=form)
