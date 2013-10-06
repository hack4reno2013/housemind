from flask.ext.restful import reqparse
zone_parser = reqparse.RequestParser()
zone_args = [('ParcelNumber',str,''),
             ('CardNumber', str,''),
             ('TempZoning', str,''),
             ('Zoning', str,''),
             ('ZoningPercent',str,'')]

for arg in zone_args:
    zone_parser.add_argument(arg[0],type=arg[1],help=arg[2])
