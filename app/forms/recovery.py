from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RecoveryRequestForm(FlaskForm):
    identifier = StringField('E-mail ou Telefone', validators=[DataRequired()])
    submit = SubmitField('Recuperar acesso')
