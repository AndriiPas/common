from flask import json, request
from flask_restful import Api, Resource, fields, marshal_with, reqparse

from db import db
from res.model.tenants_model import TenantsModel, AddressModel
from res.tenants.structure import structure_city, structure_tenants


class HotelTenants(Resource):
    @marshal_with(structure_tenants)
    def get(self, passport_id=None):
        if passport_id:
            return TenantsModel.query.get(passport_id)
        return TenantsModel.query.all()

    @marshal_with(structure_tenants)
    def post(self):
        data = json.loads(request.data)
        for i in data:
            staff = TenantsModel(**i)
            db.session.add(staff)
            db.session.commit()
        return "ok"

    @marshal_with(structure_tenants)
    def put(self, passport_id):
        data = json.loads(request.data)[0]
        tenants = TenantsModel.query.get(passport_id)
        tenants.name = data.get('name')
        tenants.passport_id = data.get('passport_id')
        tenants.age = data.get('age')
        tenants.sex = data.get('sex')
        db.session.commit()
        return "add complete"

    @marshal_with(structure_tenants)
    def delete(self, passport_id):
        data = TenantsModel.query.get(passport_id)
        db.session.delete(data)
        db.session.commit()
        return "delete"


class AdressTenants(Resource):
    @marshal_with(structure_city)
    def get(self, number=None):
        if number:
            return AddressModel.query.get(number)
        return AddressModel.query.all()

    @marshal_with(structure_city)
    def post(self):
        data = json.loads(request.data)
        for i in data:
            staff = AddressModel(**i)
            db.session.add(staff)
            db.session.commit()
        return "ok"

    @marshal_with(structure_city)
    def delete(self, number):
        data = TenantsModel.query.get(number)
        db.session.delete(data)
        db.session.commit()
        return "delete"
