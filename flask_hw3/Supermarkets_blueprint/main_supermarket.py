import os
import uuid

from flask import Blueprint, render_template, request, session, abort
from werkzeug.utils import redirect, secure_filename
from Supermarkets_blueprint.supermarkets_list import supermarkets_list
from Supermarkets_blueprint.form import AddSupermarket

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates', static_folder="static_sm")


@supermarkets.route('/supermarket/<num>')
def get_supermarket(num):
    for supermarket in supermarkets_list:
        if supermarket["id"] == num:
            session['supermarket' + num] = True
            return render_template('supermarket.html', supermarket=supermarket)
    abort(404)


@supermarkets.route('/add_supermarket', methods=['GET', 'POST'])
def get_add_supermarket():
    form = AddSupermarket()
    img = False
    if request.method == "POST":
        if form.validate_on_submit():
            if request.files['file']:
                img = request.files['file']
                if img:
                    filename = secure_filename(img.filename)
                    img.save(os.path.join('Supermarkets_blueprint/static_sm', filename))
                    img.close()
            data = {
                'id': uuid.uuid4().hex,
                'name': form.name.data,
                'Location': form.location.data,
                'img_name': secure_filename(img.filename) if img else '',
                }
            supermarkets_list.append(data)
            print(supermarkets_list)
            return redirect('/all_supermarkets')
    return render_template("add_supermarket.html", title=AddSupermarket, form=form)


@supermarkets.route('/all_supermarkets')
def get_all_supermarket():
    result = []
    if request.query_string:
        location = request.args.get('location')
        for i in supermarkets_list:
            #print(location[1:-1] == i["location"])
            if location[1:-1] == i["location"]:
                result.append(i)
    else:
        result = supermarkets_list
    for supermarket in result:
        if session.get('supermarket' + supermarket['id']):
            supermarket['url_check'] = True
    return render_template('all_supermarkets.html', supermarkets=result)



