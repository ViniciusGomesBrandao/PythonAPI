from flask import request
from flask_restful import Resource

class Users(Resource):
    def get(this):
        return {
            "success": True,
            "method": "GET"
        }
    def post(this):
        return {
            "success": True,
            "method": "POST"
        }

