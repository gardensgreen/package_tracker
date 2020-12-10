from flask import Flask, render_template, redirect, url_for
from config import Configuration as Config
from app.shipping_form import ShippingForm
from flask_migrate import Migrate 
from app.models import db, Package
from map.map import map

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return "<h1>Package Tracker</h1>"


@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    form.origin.choices = [(city, city) for city in map.keys()]
    form.destination.choices = [(city, city) for city in map.keys()]

    if form.validate_on_submit():
        print(form.data)
        data = form.data
        new_package = Package(
            sender=data["sender_name"],
            recipient=data["recipient_name"],
            origin=data["origin"],
            destination=data["destination"],
            location=data["origin"]
        )
        db.session.add(new_package)
        db.session.commit()
        return redirect(url_for(".index"))

    return render_template('shipping_request.html', form=form)
