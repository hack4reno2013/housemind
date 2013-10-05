from flask import Flask
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Property(Resource):
    def get():
        pass

class Area(Resource):
    def get():
        pass

class Building(Resource):
    def get():
        pass

class Drawn(Resource):
    def get():
        pass

class Misc(Resource):
    def get():
        pass

class Sales(Resource):
    def get():
        pass


class Zoning(Resource):
    def get():
        pass


if __name__ == '__main__':
    app.run(debug=True)



