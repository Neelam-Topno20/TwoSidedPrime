from flask import Blueprint
from flask_restful import Api
from controller.Hello import Hello
from controller.FindTSP import FindTSP

# Creating a blueprint container for the flask app
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# All the Routes for this Restful API
api.add_resource(Hello, '/Hello')
api.add_resource(FindTSP, '/FindTSP')
