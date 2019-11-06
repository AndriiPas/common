from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect

from Products_blueprint.js_open import get_len
from Products_blueprint.form import AddProduct

products = Blueprint('products', __name__, template_folder='templates')

@products.route('/product')
def get_all_products():
    length = get_len()
    return render_template('all_products.html', lenght_json=length)


@products.route('/add_product', methods=['GET', 'POST'])
def get_add_product():
    form = AddProduct()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.id_.data, form.name.data, form.description.data, form.img_name.data, form.price.data))
        return redirect('/product')
    return render_template("add_product.html", title=AddProduct, form=form)

