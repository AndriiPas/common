from flask import Blueprint
from flask_restful import Api
from res.room.main_room import HotelRooms, RoomStaff

room = Blueprint('room', __name__)
api = Api(room)

api.add_resource(HotelRooms, "/rooms", "/rooms/<number>")
api.add_resource(RoomStaff, "/roomstaff")