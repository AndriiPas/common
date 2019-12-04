from flask_restful import fields
from res.room.structure import structure_rooms

structure_city = {
    "city": fields.String,
    "street": fields.String
}


structure_tenants = {
    "name": fields.String,
    "passport_id": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "address": fields.Nested(structure_city),
    "room": fields.Nested(structure_rooms)
}