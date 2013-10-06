from flask import Flask
from flask.ext.restful import Resource, Api
from property_arg_parser import property_parser
from area_arg_parser import area_parser
from building_arg_parser import building_parser
from zone_arg_parser import zone_parser

app = Flask(__name__)
api = Api(app)

class Property(Resource):
    def get(self, **kwargs):
        args = property_parser.parse_args()
        return { 'Property' : 'coming soon!'}, 201

class Area(Resource):
    def get(self):
        args = area_parser.parse_args()
        return { 'Area' : 'coming soon!'}


class Building(Resource):
    def get(self):
        args = building_parser.parse_args()
        return { 'Building' : 'coming soon!'}
    
class Sales(Resource):
    def get(self):
        args = sales_parser.parse_args()
        return { 'Sales' : 'coming soon!'}

class Zoning(Resource):
    def get():
        args = zone_parser.parse_args()
        return { 'Zoning' : 'coming soon!'}

api.add_resource(Property,'/Property/')
api.add_resource(Area,'/Area/')
api.add_resource(Building,'/Building/')
api.add_resource(Sales,'/Sales/')
api.add_resource(Zoning,'/Zoning/')

if __name__ == '__main__':
    app.run(debug=True)



