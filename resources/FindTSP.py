from flask import request
from flask_restful import Resource


class FindTSP(Resource):

    def post(self):
        number = int(request.args.get('number'))
        if(number <= 1):
            return{'status': "false"}
        for i in range(2, number):
            if(number % i == 0):
                return{'status': "false"}
        tmp = number
        count = 0;
        tmp = int(tmp/10)
        while(tmp != 0):
            count = count+1
            print(tmp)
            if(tmp <= 1):
                return{'status': "false"}
            for i in range(2, tmp):
                if(tmp % i == 0):
                    return{'status': "false"}
            tmp = int(tmp/10)

        tmp=number
        if(int(tmp/10)!=0):
            tmp=tmp%(10*count)
        else:
            tmp=0;
        while(tmp!=0):
            print(tmp)
            count=count-1
            if(tmp <= 1):
               return{'status': "false"}
            for i in range(2, tmp):
               if(tmp % i == 0):
                   return{'status': "false"}
            if(int(tmp/10) == 0):
                tmp=0;
            else:
                tmp=tmp%(10*count)

        return{'status': "true"}
