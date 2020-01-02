from flask_restful import Resource


# A Dummy Controller Class
class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}
