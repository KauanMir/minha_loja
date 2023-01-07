from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nome = StringField('Nome', [validators.Length(min=4, max=25)])
    usuario = StringField('Usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    senha = PasswordField('Digite Sua Senha', [
        validators.DataRequired(),
        validators.EqualTo('Confirmar sua senha', message='sua senha e confirmação não são iguais')
    ])
    confirmacao = PasswordField('Digite sua senha novamente')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])