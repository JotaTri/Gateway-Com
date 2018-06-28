##############################################
# Servidor Web com APIs de controle de servicos e devices de um Gateway
# Autores :   -João Tribouillet Marcial de Menezes
#             -Pedro Henrique Lira da Costa
##############################################
from flask import Flask
from flask_restful import Api
from handlers.formula_receiver import Receiver

app = Flask(__name__)

api = Api(app)

# Classes a serem chamadas e seus respectivos endpoints
api.add_resource(Receiver, '/formula')

if __name__ == '__main__':
   app.run(host='0.0.0.0', threaded=True)
