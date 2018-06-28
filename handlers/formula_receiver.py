from flask_restful import Resource, reqparse, request
import requests
import os
from core.formula import Formula
import signal

# Classe responsavel por receber e gerenciar servicos de formulas
class Receiver(Resource):
    def __init__(self):
        self.activeFormulas = {}
        # signal.signal(signal.SIGINT, self.StopTimers)

    def get(self):
        return 'not Allowed'

    # Metodo que recebe um post contendo a formula a ser executada e o caminho a
    # ser publicado a resposta por MQTT
    def post(self):
        data = (request.get_json())

        formula = Formula().getFormula(data['formula'].encode('utf8'))
        formula.topico = data['topico'].encode('utf8')
        # self.activeFormulas[data['topico'].encode('utf8')] = formula.master_formula
        print str({'status' :200, 'message': 'Formula Received and Recognized'})
        return {'status' :200, 'message': 'Formula Received and Recognized'}


    #TODO - controle das formulas - possibilidade de excluir ou modificar um servico
    def StopTimers(self):
        print 'Terminado'
        os.exit(1)
