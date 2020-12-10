from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, SelectField, SubmitField)
from wtforms.validators import DataRequired


class ShippingForm(FlaskForm):
    sender_name = StringField("Sender Name", [DataRequired()])
    recipient_name = StringField("Recipient Name", [DataRequired()])
    origin = SelectField("Origin", [DataRequired()])
    destination = SelectField("Destination", [DataRequired()])
    express = BooleanField("Express Shipping?", [
                           DataRequired()], default=False)
