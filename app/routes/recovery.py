# routes/login.py
import secrets
from datetime import datetime, timedelta
from app.forms.recovery import RecoveryRequestForm
import pywhatkit as kit
from datetime import datetime

@login_bp.route("/recovery", methods=["GET", "POST"])
def recovery():
    form = RecoveryRequestForm()
    if form.validate_on_submit():
        # Aqui você pode enviar o link ou código por WhatsApp ou e-mail
        flash("Código de recuperação enviado!", "info")
        return redirect(url_for("login.reset_password"))
    return render_template("recovery_request.html", form=form)


if form.validate_on_submit():
    identifier = form.identifier.data.strip()
    user = User.query.filter((User.email == identifier) | (User.phone == identifier)).first()

    if user:
        token = secrets.token_urlsafe(16)
        user.reset_token = token
        user.reset_token_expiration = datetime.utcnow() + timedelta(minutes=15)
        db.session.commit()

        # Link com o token (caso vá por link)
        reset_link = url_for('login.reset_password', token=token, _external=True)

        # Enviar WhatsApp
        send_whatsapp(user.phone, f"Olá {user.name}, acesse para redefinir sua senha: {reset_link}")

        flash("Link de recuperação enviado por WhatsApp!", "info")
        return redirect(url_for("login.login"))
    else:
        flash("Usuário não encontrado", "danger")


def send_whatsapp(phone_number, message):
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 2  # Envia com 2 minutos de margem

    # Corrigir número (DDI e DDD)
    formatted_number = phone_number
    if not phone_number.startswith("+"):
        formatted_number = "+55" + phone_number  # Brasil

    try:
        kit.sendwhatmsg(formatted_number, message, hour, minute, wait_time=10, tab_close=True)
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {e}")
