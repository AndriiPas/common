from flask import request, json
from flask_restful import Resource, marshal_with

from db import db
from res.model.room_model import RoomModel
from res.model.staff_model import StaffModel
from res.room.structure import structure_rooms


class HotelRooms(Resource):
    @marshal_with(structure_rooms)
    def get(self, number=None):
        if number:                                     # ЯКЩО ТРУ
            data = RoomModel.query.get(number)         # ТО ДАЄМО ЛИШЕ З ПОТРІБНИМ ЗНАЧЕННЯМ
            return data
        return RoomModel.query.all()

    @marshal_with(structure_rooms)
    def post(self):
        data = json.loads(request.data)    # ЗАВАНТАЖУЄМО ДАНІ В DATA
        for i in data:                     # ПРОБІГАЄМОСЯ ПО ЦИКЛІ... ПЕРЕВІРКА НА СПИСОК ДАНИХ
            room = RoomModel(**i)
            db.session.add(room)           # ДОДАЄМО ДАНІ В СЕСІЮ
            db.session.commit()            # І КОММІТИМ
        return data

    @marshal_with(structure_rooms)
    def put(self, number):
        data = json.loads(request.data)[0]
        post = RoomModel.query.get(number)
        post.level = data.get("level")
        post.status = data.get("status")
        post.price = data.get("price")
        post.tenant_id = data.get("tenant_id")
        db.session.commit()
        return "add complete"

    @marshal_with(structure_rooms)
    def delete(self, number):
        post = RoomModel.query.get(number)
        db.session.delete(post)
        db.session.commit()
        return "delete"


class RoomStaff(Resource):
    def post(self):
        data = json.loads(request.data)
        staff_id = data.get("staff_id")
        room_id = data.get("room_id")
        staff = StaffModel.query.filter_by(number=staff_id).first()
        room = RoomModel.query.filter_by(number=room_id).first()
        room.staff_id.append(staff)
        db.session.commit()
        return f"Added {staff_id} to {room_id}"


