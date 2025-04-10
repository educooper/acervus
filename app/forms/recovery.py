from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class VerificationCodeForm(FlaskForm):
    code = StringField('Código de Verificação', validators=[DataRequired(), Length(min=6, max=6)])
    submit = SubmitField('Verificar')

class RecoveryRequestForm(FlaskForm):
    phone = StringField("Telefone cadastrado", validators=[DataRequired()])
    submit = SubmitField("Enviar código")
