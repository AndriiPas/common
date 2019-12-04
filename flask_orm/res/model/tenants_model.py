from db import db


class TenantsModel(db.Model):
    __tablename__ = 'tenants'

    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passport_id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    age = db.Column(db.String(120))
    sex = db.Column(db.String(120))
    address = db.relationship("AddressModel", backref="address")
    room = db.relationship("RoomModel", backref="room")


class AddressModel(db.Model):
    __tablename__ = 'address'

    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(80))
    street = db.Column(db.String(80))
    tenants_id = db.Column(db.Integer, db.ForeignKey("tenants.number"))



