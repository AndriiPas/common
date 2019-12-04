from flask_restful import fields

structure_staff = {
    "number": fields.Integer,
    "name": fields.String,
    "passport_id": fields.Integer,
    "position": fields.String,
    "salary": fields.Integer
}