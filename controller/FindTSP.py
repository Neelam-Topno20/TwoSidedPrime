from flask import request
from flask_restful import Resource
from service.FindTSPService import FindTSPService


# Controller class for calculating two sided prime
class FindTSP(Resource):

    # Get method which takes input integer as params to calculate two sided prime
    # Sample URL - http://127.0.0.1:5000/pyrestapi/FindTSP?number=53
    def get(self):
        try:
            number = int(request.args.get('number'))
            if FindTSPService.find_tsp_service(number):
                return {'Two Sided Prime': "true"}
            else:
                return {'Two Sided Prime': "false"}
        except ValueError:
            return {'message' :"Invalid value passed. Pass Integer value"}


