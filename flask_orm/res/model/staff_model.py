from db import db



class StaffModel(db.Model):
    __tablename__ = 'staff'

    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passport_id = db.Column(db.Integer)
    name = db.Column(db.String(80))
    position = db.Column(db.String(120))
    salary = db.Column(db.String(120))
