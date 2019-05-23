from flask import Blueprint
from flask_restful import Api

from app.modulo.oi import Oi


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Oi, '/oi')
