from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome Completo', [validators.Length(min=4, max=25)])
    username = StringField('Usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email Princial', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha e Confirmacao nao sao iguais')
    ])
    confirm = PasswordField('Repete a senha')

class LoginFormulario(Form):
    email = StringField('Email Princial', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [ validators.DataRequired()])
