from app.models import db
from flask import render_template, flash, redirect, url_for, request, session, Blueprint
from flask_login import current_user,login_required
from app.models.users import User
from app.models.coins import Coin
from app.forms.coins import AddForm
import os

coins = Blueprint('coin', __name__)



@coins.route('/coin/add', methods=['GET', 'POST'])
@login_required
def add_coin():
    form = AddForm()
    if form.validate_on_submit():
        new_coin = Coin(name=form.name.data,value=form.value.data,user_id=current_user.id)
        db.session.add(new_coin)
        db.session.commit()
        flash('Vous avez ajouté une nouvelle monnaie')
        return redirect(url_for('coin.list_coins'))
    return render_template('coins/add_coins.html', form=form,title='Ajouter une nouvelle monnaie')
   
@coins.route('/coin')
@login_required
def list_coins():
        coins = Coin.query.filter_by(user_id=current_user.id).all()
        return render_template('coins/list_coins.html', coins=coins,title='Mes monnaies')

@coins.route('/coin/<int:coin_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_coin(coin_id):
    coin = Coin.query.get_or_404(coin_id)
    if coin.user_id == current_user.id:
        db.session.delete(coin)
        db.session.commit()
        flash('Vous avez supprimé une monnaie')
        return redirect(url_for('coin.list_coins'))
    else:
        flash('Vous n\'avez pas le droit de supprimer cette monnaie')
        return redirect(url_for('coin.list_coins'))

@coins.route('/coin/<int:coin_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_coin(coin_id):
    coin = Coin.query.get_or_404(coin_id)
    if coin.user_id == current_user.id:
        form = AddForm()
        if form.validate_on_submit():
            coin.name = form.name.data
            coin.value = form.value.data
            db.session.commit()
            flash('Vous avez modifié une monnaie')
            return redirect(url_for('coin.list_coins'))
    return render_template('coins/edit_coins.html',coin_id = coin.id, form=form,title='Modifier une monnaie')
