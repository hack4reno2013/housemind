from flask.ext.restful import reqparse
building_parser = reqparse.RequestParser()
building_args = [('ParcelNumber', str, "comming soon"),
                 ('PropertyName', str,""),
                 ('Buildingtype', str,""),
                 ('CardNumber', str,""),
                 ('QualityClass', str,""),
                 ('OrigConstructionYear', int,""),
                 ('AverConstructionYear', int,""),
                 ('NoofUnits', int,""),
                 ('Stories', str,""),
                 ('ExteriorWallsType1', str,""),
                 ('ExteriorPercent1', float,""),
                 ('ExteriorWallsType2', str,""),
                 ('ExteriorPercent2', float,""),
                 ('AvgStoryHeight', float,""),
                 ('Roofing', str,""),
                 ('HeatPercent', float,""),
                 ('HeatCool1', str,""),
                 ('HeatCoolPercent1',float,""),
                 ('HeatCool2', str,""),
                 ('HeatCoolPercent2', float,""),
                 ('Baths', float,""),
                 ('PlumbFixtures', int,""),
                 ('Bedrooms', int,""),
                 ('Shape', int,""),
                 ('BasementGarage', int,"")]

for arg in building_args:
    building_parser.add_argument(arg[0],type=arg[1],help=arg[2])
