from flask import Flask, render_template, redirect, url_for
from config import Configuration as Config
from app.shipping_form import ShippingForm
from map.map import map

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def index():
    return "<h1>Package Tracker</h1>"


@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    form.origin.choices = [(city, city) for city in map.keys()]
    form.destination.choices = [(city, city) for city in map.keys()]

    if form.validate_on_submit():
        return redirect(url_for(".index"))

    return render_template('shipping_request.html', form=form)
