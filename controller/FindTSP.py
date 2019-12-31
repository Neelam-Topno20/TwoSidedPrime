from flask import request
from flask_restful import Resource
from service.FindTSPService import FindTSPService


class FindTSP(Resource):

    def get(self):
        number = int(request.args.get('number'))
        if FindTSPService.find_tsp_service(number):
            return {'status': "true"}
        else:
            return {'status':"false"}

