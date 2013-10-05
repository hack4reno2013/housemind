from flask.ext.restful import reqparse
area_parser = reqparse.RequestParser()
area_args = [('ParcelNumber', str, 'comming soon'),
('CardNumber', str, 'comming soon'),
('Sequence', str, 'comming soon'),
('Area', str, 'comming soon'),
('PercentUsable', str, 'comming soon'),
('AlternateType', str, 'comming soon'),
('AlternatePercentage', str, 'comming soon'),
('Quality', str, 'comming soon')]

for arg in area_args:
    area_parser.add_argument(arg[0],type=arg[1],help=arg[2])

