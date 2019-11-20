from flask import Flask, render_template, session
from werkzeug.utils import redirect

from Products_blueprint.main_products import products
from Supermarkets_blueprint.main_supermarket import supermarkets

app = Flask(__name__)
app.register_blueprint(products)
app.register_blueprint(supermarkets)
app.config['SECRET_KEY'] = 'password'
to_reload = False

@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/delete-visits')
def delete_visits():
    session.clear()
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('E404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)