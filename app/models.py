from flask_sqlalchemy import SQLAlchemy
from map.map import advance_delivery, DELIVERED
# from ..package_tracker import app

db = SQLAlchemy()


class Package(db.Model):
    __tablename__ = "packages"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(20), nullable=False)
    recipient = db.Column(db.String(20), nullable=False)
    origin = db.Column(db.String(20), nullable=False)
    destination = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable=False)

    @staticmethod
    def advance_all_locations():
        packages = Package.query.all()
        for package in packages:
            if package.location is not DELIVERED:
                package.location = advance_delivery(package.location,
                                                    package.destination)

        db.session.commit()
