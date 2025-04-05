from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message="O campo email é obrigatório."),
        Email(message="Informe um email válido.")
    ])
    
    password = PasswordField('Senha', validators=[
        DataRequired(message="O campo senha é obrigatório."),
        Length(min=6, message="A senha deve ter pelo menos 6 caracteres.")
    ])

    submit = SubmitField('Entrar')
