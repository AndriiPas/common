from flask import Blueprint
from flask_restful import Api
from res.tenants.main_tenants import HotelTenants, AdressTenants

tenants = Blueprint('tenants', __name__)
api = Api(tenants)

api.add_resource(HotelTenants, "/tenants", "/tenants/<passport_id>")
api.add_resource(AdressTenants, "/address", "/address/<number>")