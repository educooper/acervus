# forms/verify_code.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class VerificationCodeForm(FlaskForm):
    code = StringField("Código recebido", validators=[
        DataRequired(), Length(min=6, max=6)
    ])
    submit = SubmitField("Validar Código")
