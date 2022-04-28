from app.models import db
from flask import render_template, flash, redirect, url_for, request, session, Blueprint
from flask_login import current_user,login_required
from app.models.users import User
from app.models.coins import Coin
from app.forms.coins import AddForm

coins = Blueprint('coin', __name__)

@coins.route('/coin/add', methods=['GET', 'POST'])
@login_required
def add_coin():
    form = AddForm()
    if form.validate_on_submit():
        new_coin = Coin(name=form.name.data, symbol=form.symbol.data, user_id=current_user.id)
        db.session.add(new_coin)
        db.session.commit()
        flash('Vous avez ajouté une nouvelle monnaie')
        return redirect(url_for('coins.list_coins'))
    return render_template('coins/add_coins.html', form=form,title='Ajouter une nouvelle monnaie')
   
@coins.route('/coin')
@login_required
def list_coins():
        coins = Coin.query.filter_by(user_id=current_user.id).all()
        return render_template('coins/list_coins.html', coins=coins,title='Mes monnaies')
    