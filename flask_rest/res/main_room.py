from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with, reqparse


room = Blueprint('room', __name__)
api = Api(room)


class Rooms:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


structure_rooms = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer
}

rooms_list = [Rooms(1, 1, "available", 1200),
              Rooms(2, 1, "closed", 900),
              Rooms(3, 2, "closed", 1000),
              Rooms(4, 2, "closed", 1000)
              ]

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('number', type=int, help='Integer!')
parser.add_argument('status', type=str, help='closed or available; only str!')


class HotelRooms(Resource):
    @marshal_with(structure_rooms)
    def get(self):
        args = parser.parse_args()
        if args["number"]:
            for i in rooms_list:
                if i.number == int(args["number"]):
                    return i
        result = []
        if args['status']:
            for i in rooms_list:
                if i.status == args['status']:
                    result.append(i)
            return result
        return rooms_list

    @marshal_with(structure_rooms)
    def post(self):
        data = json.loads(request.data)
        number = data.get('number')
        level = data.get('level')
        status = data.get('status')
        price = data.get('price')
        rooms_list.append(Rooms(number, level, status, price))


    @marshal_with(structure_rooms)
    def patch(self):
        data = json.loads(request.data)
        number = data.get('number')
        level = data.get('level')
        status = data.get('status')
        price = data.get('price')
        for i in rooms_list:
            if i.number == number:
                rooms_list.remove(i)
        rooms_list.append(Rooms(number, level, status, price))

    @marshal_with(structure_rooms)
    def delete(self, number):
        for i in rooms_list:
            if i.number == number:
                rooms_list.remove(i)
                break
        return 'false'


api.add_resource(HotelRooms, "/rooms", "/rooms/<number>")
