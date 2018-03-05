from flask_restful import Resource, Api

hello = {}

class Login(Resource):
    def post(self):
        return {'post': 'is availoable'}
