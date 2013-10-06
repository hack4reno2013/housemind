from flask.ext.restful import reqparse
from extra_types import int_range, float_range

building_parser = reqparse.RequestParser()
building_args = [('ParcelNumber', str, "comming soon"),
                 ('PropertyName', str,""),
                 ('Buildingtype', str,""),
                 ('CardNumber', str,""),
                 ('QualityClass', str,""),
                 ('OrigConstructionYear', int_range,""),
                 ('AverConstructionYear', int_range,""),
                 ('NoofUnits', int_range,""),
                 ('Stories', str,""),
                 ('ExteriorWallsType1', str,""),
                 ('ExteriorPercent1', float_range,""),
                 ('ExteriorWallsType2', str,""),
                 ('ExteriorPercent2', float_range,""),
                 ('AvgStoryHeight', float_range,""),
                 ('Roofing', str,""),
                 ('HeatPercent', float_range,""),
                 ('HeatCool1', str,""),
                 ('HeatCoolPercent1',float_range,""),
                 ('HeatCool2', str,""),
                 ('HeatCoolPercent2', float_range,""),
                 ('Baths', float_range,""),
                 ('PlumbFixtures', int_range,""),
                 ('Bedrooms', int_range,""),
                 ('Shape', int_range,""),
                 ('BasementGarage', int_range,"")]

for arg in building_args:
    building_parser.add_argument(arg[0],type=arg[1],help=arg[2])
