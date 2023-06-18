from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'data': 'Hello,world'}


class HelloName(Resource):
    def get(self, name):
        return {'data': 'Hello, {}'.format(name)}


api.add_resource(HelloWorld, '/helloworld')
api.add_resource(HelloName, '/helloworld/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)