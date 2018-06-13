from flask_restful import Resource, reqparse, request
import requests
import os
from core.formula import Formula
import signal

class Receiver(Resource):
    def __init__(self):
        self.activeFormulas = {}
        # signal.signal(signal.SIGINT, self.StopTimers)

    def get(self):
        return 'pra que get?'

    def post(self):
        data = (request.get_json())

        # formula = Formula().getFormula(data['formula'].encode('utf8'))
        # formula.topico = data['topico'].encode('utf8')
        # self.activeFormulas[data['topico'].encode('utf8')] = formula.master_formula
        # print self.activeFormulas
        print str({'status' :200, 'message': 'Formula Received and Recognized'})
        return {'status' :200, 'message': 'Formula Received and Recognized'}

    def StopTimers(self):
        print 'Terminado'
        os.exit(1)
