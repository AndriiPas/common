from flask import request, json
from flask_restful import Resource, marshal_with

from db import db
from res.model.staff_model import StaffModel
from res.staff.structure import structure_staff


class HotelStaff(Resource):
    @marshal_with(structure_staff)
    def get(self, number=None):
        if number:
            data = StaffModel.query.get(number)
            return data
        return StaffModel.query.all()

    @marshal_with(structure_staff)
    def post(self):
        data = json.loads(request.data)
        for i in data:
            staff = StaffModel(**i)
            db.session.add(staff)
            db.session.commit()
        return "ok"

    @marshal_with(structure_staff)
    def put(self, number):
        data = json.loads(request.data)[0]
        staff = StaffModel.query.get(number)
        staff.passport_id = data.get("passport_id")
        staff.name = data.get("name")
        staff.position = data.get("position")
        staff.salary = data.get("salary")
        db.session.commit()
        return "add complete"

    @marshal_with(structure_staff)
    def delete(self, number):
        data = StaffModel.query.get(number)
        db.session.delete(data)
        db.session.commit()
        return "delete"
