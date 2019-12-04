from flask import Blueprint
from flask_restful import Api
from res.staff.main_staff import HotelStaff

staff = Blueprint('staff', __name__)
api = Api(staff)

api.add_resource(HotelStaff, "/staff", "/staff/<number>")