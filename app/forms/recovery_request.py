# forms/recovery_request.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

class RecoveryRequestForm(FlaskForm):
    phone = StringField("Telefone (somente números)", validators=[
        DataRequired(),
        Regexp(r'^\d{10,11}$', message="Informe um telefone válido com DDD.")
    ])
    submit = SubmitField("Enviar Código")
