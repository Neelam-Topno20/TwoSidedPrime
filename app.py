from flask import Blueprint
from flask_restful import Api
from controller.Hello import Hello
from controller.FindTSP import FindTSP

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(FindTSP, '/FindTSP')
