from flask_restful import Resource, reqparse, request
import requests

class Receiver(Resource):

    def get(self):
        return 'pra que get?'

    def post(self):
        data = (request.get_json())
        

        return {'status' :200, 'message': 'Formula Received and Recognized'}
