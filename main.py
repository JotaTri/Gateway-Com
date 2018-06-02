from flask import Flask
from flask_restful import Api
from handlers.formula_receiver import Receiver

app = Flask(__name__)

api = Api(app)


api.add_resource(Receiver, '/formula')
# @app.route('/')
# def hello_world():
#    return 'Hello World'

if __name__ == '__main__':
   app.run(host='0.0.0.0')
