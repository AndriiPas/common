from flask import Blueprint, request
from flask_restful import Api, Resource, fields, marshal_with, reqparse


tenants = Blueprint('tenants', __name__)
api = Api(tenants)


class Tenants:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number


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
    "room_number": fields.Integer
}

tenants_list = [Tenants("Oleg", "2596485956", 26, "men", {"city": "Kiev", "street": "Bogdanivska"}, 2),
                Tenants("Vasia", "8856995472", 65, "men", {"city": "Lviv", "street": "Pidgolosko"}, 3),
                Tenants("Elsa", "6522418895", 18, "women", {"city": "Kiev", "street": "Lvivska"}, 4)
                ]


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('passport_id', type=str, help='String!')


class Tenants(Resource):
    @marshal_with(structure_tenants)
    def get(self):
        args = parser.parse_args()
        if args["passport_id"]:
            for i in tenants_list:
                if i.passport_id == args["passport_id"]:
                    return i
        return tenants_list

    @marshal_with(structure_tenants)
    def patch(self):
        data = request.json
        name = data.get('name')
        passport_id = data.get('passport_id')
        age = data.get('age')
        sex = data.get('sex')
        address = data.get('address')
        room_number = data.get('room_number')
        for i in tenants_list:
            if i.passport_id == passport_id:
                tenants_list.remove(i)
        tenants_list.append(Tenants(name, passport_id, age, sex, address, room_number))

    @marshal_with(structure_tenants)
    def delete(self, passport_id):
        for i in tenants_list:
            if i.passport_id == passport_id:
                tenants_list.remove(i)
                break
        return 'false'


api.add_resource(Tenants, "/tenants", "/tenants/<passport_id>")
