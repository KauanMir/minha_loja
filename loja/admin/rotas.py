from flask import redirect, render_template, session, request, url_for, flash
from loja.produtos.models import AddProduto
from loja import app, db, bcrypt
from loja.admin.formulario import LoginFormulario, RegistrationForm
from loja.admin.models import User
import os



@app.route('/')
def admin():
    if 'email' not in session:
        flash(f'Favor fazer seu login no sistema primeiro', 'danger')
        return redirect(url_for('login'))
    produtos = AddProduto.query.all()
    return render_template('admin/index.html', title='Pagina Administrativa', produtos=produtos)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.name.data} por registrar', 'success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', title="Registrar Usuarios", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email= form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Olá {form.email.data}, logado com sucesso!', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('E-mail ou senha errado')
    return render_template('admin/login.html', form=form ,title='Pagina Login')