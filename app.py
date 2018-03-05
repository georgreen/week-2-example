from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.errorhandler(404)
def page_not_found(e):
    return "{'erro': 'resource not found'}", 404


# method using flask-restfull
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200

    def post(self):
        return {'post': 'is availoable'}, 201

    def put(self):
        return {'put': 'Is working'}, 201

api.add_resource(HelloWorld, '/hello') # add urls


# flask flat way
@app.route('/helloworld', methods=['GET', 'POST']) # add urls
def hello():
    if request.method == 'GET':
        return "{'Hello': 'World'}", 200

    if request.method == 'POST':
        return "{'Hello': 'From post'}", 201

if __name__ == '__main__':
    app.run(debug=True)
