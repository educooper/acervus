# forms/article_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectMultipleField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class ArticleForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    year = IntegerField('Ano', validators=[DataRequired()])
    file = FileField('PDF', validators=[FileAllowed(['pdf'], 'Apenas arquivos PDF!')])
    tags = SelectMultipleField('Tags', coerce=int)  # IDs das tags
    submit = SubmitField('Salvar')
