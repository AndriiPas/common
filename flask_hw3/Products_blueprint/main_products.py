import os
import uuid

from flask import Blueprint, render_template, request, session, abort
from werkzeug.utils import redirect, secure_filename
from Products_blueprint.products_list import products_list
from Products_blueprint.form import AddProduct

products = Blueprint('products', __name__, template_folder='templates', static_folder='static')


@products.route('/product/<num>')
def get_product(num):
    for product in products_list:
        if product["id"] == num:
            session['product' + num] = True
            return render_template('product.html', product=product)
    abort(404)


@products.route('/add_product', methods=['GET', 'POST'])
def get_add_product():
    form = AddProduct()
    img = False
    if request.method == "POST":
        if form.validate_on_submit():
            if request.files['file']:
                img = request.files['file']
                print(img)
                if img:
                    filename = secure_filename(img.filename)
                    img.save(os.path.join('static', filename))
                    img.close()
            data = {
                'id': uuid.uuid4().hex,
                'name': form.name.data,
                'description': form.description.data,
                'img_name': secure_filename(img.filename) if img else '',
                'price': str(form.price.data)
                   }
            products_list.append(data)
            print(products_list)
            return redirect('/all_product')
    return render_template("add_product.html", title=AddProduct, form=form)


@products.route('/all_product')
def get_all_products():
    result = []
    if request.query_string:
        price = request.args.get('price')
        for i in products_list:
            if int(price) == int(i["price"]):
                result.append(i)
    else:
        result = products_list

    for product in result:
        if session.get('product' + product['id']):
            product['url_check'] = True
    return render_template('all_products.html', products=result)


@products.route('/delete-visits')
def delete_visits():
    session.clear()
    for key in session.keys():
        session.pop(key)
    return 'Visits deleted'
