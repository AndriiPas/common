from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with, reqparse


staff = Blueprint('staff', __name__)
api = Api(staff)


class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


structure_staff = {
    "name": fields.String,
    "passport_id": fields.Integer,
    "position": fields.String,
    "salary": fields.Integer
}

staff_list = [Staff("Leon", "2906158648", "Administrator", 1200),
              Staff("Jane", "6958884555", "Waiter", 900)
              ]

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('passport_id', type=str, help='String!')   #  прийом аргументу з урли


class HotelStaff(Resource):
    @marshal_with(structure_staff)
    def get(self):
        args = parser.parse_args()    #присвоюємо аргумент змінній
        if args["passport_id"]:
            for i in staff_list:
                if i.passport_id == args["passport_id"]:
                    return i
        return staff_list

    @marshal_with(structure_staff)
    def post(self):
        data = json.loads(request.data)
        name = data.get('name')
        passport_id = data.get('passport_id')
        position = data.get('position')
        salary = data.get('salary')
        staff_list.append(Staff(name, passport_id, position, salary))

    @marshal_with(structure_staff)
    def patch(self):
        data = json.loads(request.data)
        name = data.get('name')
        passport_id = data.get('passport_id')
        position = data.get('position')
        salary = data.get('salary')
        for i in staff_list:
            if i.passport_id == passport_id:
                staff_list.remove(i)
        staff_list.append(Staff(name, passport_id, position, salary))

    @marshal_with(structure_staff)
    def delete(self, passport_id):
        for i in staff_list:
            if i.passport_id == passport_id:
                staff_list.remove(i)
                break
        return 'false'


api.add_resource(HotelStaff, "/staff", "/staff/<passport_id>")
