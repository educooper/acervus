from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user
from app.forms.login import LoginForm
from app.models.user import User
from app.forms.recovery import RecoveryRequestForm
from app.forms.reset_password import ResetPasswordForm
from app.forms.verify_code import VerificationCodeForm  # lembre de garantir esse form
from app.utils.helpers import gerar_codigo
from app.services.whatsapp import enviar_codigo_por_whatsapp
from app import db

login_bp = Blueprint('login', __name__)

# ----------------------------
# LOGIN NORMAL
# ----------------------------
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('E-mail ou senha inválidos.', 'danger')
    return render_template('login.html', form=form)

# ----------------------------
# SOLICITAÇÃO DE RECUPERAÇÃO
# ----------------------------
@login_bp.route("/recovery", methods=["GET", "POST"])
def recovery():
    form = RecoveryRequestForm()
    if form.validate_on_submit():
        codigo = gerar_codigo()
        telefone = form.phone.data

        # Armazena na sessão para validação posterior
        session["recovery_phone"] = telefone
        session["recovery_code"] = codigo

        enviar_codigo_por_whatsapp(telefone, codigo)

        flash("Código enviado por WhatsApp!", "info")
        return redirect(url_for("login.verify_code"))
    return render_template("recovery_request.html", form=form)

# ----------------------------
# VERIFICAÇÃO DO CÓDIGO
# ----------------------------
@login_bp.route("/verify-code", methods=["GET", "POST"])
def verify_code():
    form = VerificationCodeForm()
    telefone = session.get('recovery_phone')

    if not telefone:
        flash('Sessão expirada. Inicie a recuperação novamente.', 'danger')
        return redirect(url_for('login.recovery'))

    if form.validate_on_submit():
        user = User.query.filter_by(phone=telefone).first()
        if user and form.code.data == session.get('recovery_code'):
            session['verified_user_id'] = user.id
            flash('Código verificado com sucesso. Redefina sua senha.', 'success')
            return redirect(url_for('login.reset_password'))
        else:
            flash('Código inválido. Tente novamente.', 'danger')
    
    return render_template('verify_code.html', form=form)

# ----------------------------
# REDEFINIÇÃO DE SENHA
# ----------------------------
@login_bp.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    user_id = session.get('verified_user_id')
    if not user_id:
        flash('Acesso inválido. Inicie a recuperação novamente.', 'danger')
        return redirect(url_for('login.recovery'))

    user = User.query.get(user_id)
    form = ResetPasswordForm()

    if form.validate_on_submit():
        user.password_hash = generate_password_hash(form.password.data)
        db.session.commit()

        # Limpa sessão e código
        session.pop('verified_user_id', None)
        session.pop('recovery_code', None)
        session.pop('recovery_phone', None)

        flash('Senha atualizada com sucesso!', 'success')
        return redirect(url_for('login.login'))

    return render_template("reset_password.html", form=form)
