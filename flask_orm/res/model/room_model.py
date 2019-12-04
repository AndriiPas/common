from db import db


association_table = db.Table(
    'association_table',
    db.Column('room_id', db.Integer, db.ForeignKey('room.number')),
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.number'))
)


class RoomModel(db.Model):
    __tablename__ = "room"

    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.Integer)
    status = db.Column(db.String)
    price = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.number"))
    staff_id = db.relationship("StaffModel", secondary=association_table, backref=db.backref("room"))


