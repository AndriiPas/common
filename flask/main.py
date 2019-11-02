from flask import Flask, render_template

app = Flask(__name__)


@app.route('/base')
def get_base():
    return render_template('base.html')


@app.route('/home')
@app.route('/')
def get_home1():
    return render_template('home.html')


@app.route('/vegetables')
def get_vegetables():
    vegetable_lst = ["artichoke", "asparagus", "potato", "tomato", "cabbage", "beans", "carrot", "beetroot", "cucumber"]
    return render_template('vegetables.html', list=vegetable_lst)


@app.route('/fruits')
def get_fruits():
    fruit_lst = ["Lemons", "Lettuce", "Lima Beans", "Limes", "Longan", "melon", "apple", "strawberry", "grape"]
    return render_template('fruits.html', list=fruit_lst)


if __name__ == "__main__":
    app.run(debug=True)
