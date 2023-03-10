import secrets
from flask import redirect, render_template, session, url_for, flash, request
from loja.produtos.models import AddProduto
from .forms import Addprodutos
from loja import db, app, photos
from loja.produtos.models import Marca, Categoria, AddProduto

@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if 'email' not in session:
        flash(f'Favor fazer seu login no sistema primeiro', 'danger')
        return redirect(url_for('login'))

    if request.method == "POST":
        getmarca = request.form.get('marca')
        marcas = Marca(name=getmarca)
        db.session.add(marcas)
        flash(f'A marca {getmarca} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addmarca'))

    return render_template('/produtos/addmarca.html', marcas='marcas')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if 'email' not in session:
        flash(f'Favor fazer seu login no sistema primeiro', 'danger')
        return redirect(url_for('login'))

    if request.method == "POST":
        getcat = request.form.get('categoria')
        cat = Categoria(name=getcat)
        db.session.add(cat)
        flash(f'A categoria {getcat} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))

    return render_template('/produtos/addmarca.html')

@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    if 'email' not in session:
        flash(f'Favor fazer seu login no sistema primeiro', 'danger')
        return redirect(url_for('login'))

    marcas = Marca.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)
    if request.method=="POST":

        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.discription.data
        marca = request.form.get('marca')
        categoria = request.form.get('categoria')

        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+'.')
        image_2 =photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+'.')
        image_3 =photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+'.')

        addpro = AddProduto(name=name, price=price,discount=discount,
         stock=stock,colors=colors, desc=desc, marca_id=marca,
         categoria_id=categoria, image_1=image_1, image_2=image_2, image_3=image_3)

        db.session.add(addpro)
        flash(f'Produto {name} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('produtos/addprodutos.html', title="Cadastrar Produtos", form=form, marcas=marcas, categorias=categorias )
    