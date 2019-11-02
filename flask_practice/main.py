from flask import Flask, render_template
from utils import get_data


app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/clock')
def get_clock_page():
    arg = get_data("Alarm clock")
    return render_template("Clock.html", title=arg['title'], text=arg['text'])


@app.route('/Headphone')
def get_headphones_page():
    arg = get_data("Headphones")
    return render_template("Headphone.html", title=arg['title'], text=arg['text'])


@app.route('/ipod')
def get_ipod_page():
    arg = get_data("iPod")
    return render_template("ipod.html", title=arg['title'], text=arg['text'])


@app.route('/calculator')
def get_calculator_page():
    arg = get_data("Calculator")
    return render_template("calculator.html", title=arg['title'], text=arg['text'])


@app.route('/coffeemaker')
def get_cofeemaker_page():
    arg = get_data("Coffeemaker")
    return render_template("coffeemaker.html", title=arg['title'], text=arg['text'])


@app.route('/battery_charger')
def get_battery_charger_page():
    arg = get_data("Battery charger")
    return render_template("battery_charger.html", title=arg['title'], text=arg['text'])


if __name__ == "__main__":
    app.run(debug=True)
