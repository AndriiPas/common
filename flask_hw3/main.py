from flask import Flask, render_template, request
from Products_blueprint.main_products import products


app = Flask(__name__)
app.register_blueprint(products)
app.config['SECRET_KEY'] = 'password'

@app.route('/home')
@app.route('/')
def get_home_page():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
