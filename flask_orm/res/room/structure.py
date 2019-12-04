from flask_restful import fields

structure_rooms = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer,
    "tenant_id": fields.Integer,
    "staff_id": fields.String
}