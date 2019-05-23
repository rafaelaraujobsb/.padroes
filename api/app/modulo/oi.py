from flask_restful import Resource
from flasgger.utils import swag_from


class Oi(Resource):
    @swag_from('../../doc/api/oi_get.yml')
    def get(self):
        return {'status': 200}
