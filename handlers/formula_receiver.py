from flask_restful import Resource, reqparse, request
import requests
from core.formula import Formula

class Receiver(Resource):

    def get(self):
        return 'pra que get?'

    def post(self):
        data = (request.get_json())

        formula = Formula(data['formula'])
        print formula
        return {'status' :200, 'message': 'Formula Received and Recognized'}
