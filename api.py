from flask import Flask
from flask.ext.restful import Resource, Api
from sqlalchemy import select
from schema.schema import metadata, properties, areas, buildings, sales, zones
import schema.settings as settings
from sqlalchemy import create_engine
from api.property_arg_parser import property_parser
from api.area_arg_parser import area_parser
from api.building_arg_parser import building_parser
from api.zone_arg_parser import zone_parser
from api.sales_arg_parser import sales_parser


app = Flask(__name__)
api = Api(app)
engine = create_engine(settings.DB_STRING)

def get_select_results(s):
    data = None
    with engine.begin() as conn:
        results = conn.execute(s)
        data = params_from_query(results)
    return data

#this is going to need to clean up some type stuff later
def params_from_query(results):
        data = []
        for row in results:
            rowDict = dict(zip(row.keys(), row))
            for k in rowDict.keys():
                rowDict[k] = str(rowDict[k])
                data.append(rowDict)
        return data

def process_args_and_select(parser,table):
    args = parser.parse_args()
    s = select([table]).limit(10)
    s = get_where_clause(args,s,table)
    return get_select_results(s)


def get_where_clause(args,s,t):
    valid_args = {}
    for k in args.keys():
        if args[k] != None:
            valid_args[k] = args[k]
    print(valid_args.keys())
    for k in valid_args.keys():
        s = s.where(getattr(t.c,k) == valid_args[k])
    return s

class Property(Resource):
    def get(self):
        return process_args_and_select(propety_parser,
                                       properties)

class Area(Resource):
    def get(self):
        return process_args_and_select(area_parser,
                                       areas)

class Building(Resource):
    def get(self):
        return process_args_and_select(building_parser,
                                       buildings)
    
class Sales(Resource):
    def get(self):
        return process_args_and_select(sales_parser,
                                       sales)

class Zone(Resource):
    def get(self):
        return process_args_and_select(zone_parser,
                                       zones)

api.add_resource(Property,'/Property/')
api.add_resource(Area,'/Area/')
api.add_resource(Building,'/Building/')
api.add_resource(Sales,'/Sales/')
api.add_resource(Zone,'/Zone/')

if __name__ == '__main__':
    app.run(debug=True)



