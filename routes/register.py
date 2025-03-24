from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from flask_login import login_user
from acervus import db
from acervus.models.user import User
from acervus.forms.register import RegisterForm

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(name=form.name.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('register.html', form=form)
