from flask.ext.restful import reqparse
property_parser = reqparse.RequestParser()
property_args = [('ParcelNumber',str, 'comming soon'),
                 ('LastName', str, 'comming soon'),
                 ('FirstName', str, 'comming soon'),
                 ('EtAls', str, 'comming soon'),
                 ('SitusNumber', str, 'comming soon'),
                 ('SitusDirection', str,'comming soon'),
                 ('SitusStreet', str, 'comming soon'),
                 ('MailingAddress1', str, 'comming soon'),
                 ('MailingAddress2', str, 'comming soon'),
                 ('MailingCity', str, 'comming soon'),
                 ('MailingState', str, 'comming soon'),
                 ('MailingZipCode', str, 'comming soon'),
                 ('TaxDistrict', str, 'comming soon'),
                 ('Township', str, 'comming soon'),
                 ('Section', str,'comming soon'),
                 ('Lot', str, 'comming soon'),
                 ('Block', str, 'comming soon'),
                 ('Range', str, 'comming soon'),
                 ('Subdivision', str, 'comming soon'),
                 ('LandAppraised', str, 'comming soon'),
                 ('LandAssessed', str, 'comming soon'),
                 ('ImprovmentAppraised', str, 'comming soon'),
                 ('ImprovmentAssessed', str, 'comming soon'),
                 ('ReappraisalCycle', str, 'comming soon'),
                 ('LandUseCode', str, 'comming soon'),
                 ('Water', str, 'comming soon'),
                 ('Sewer', str, 'comming soon'),
                 ('StreetType', str, 'comming soon'),
                 ('LandArea', str, 'comming soon'),
                 ('LandUnittype', str, 'comming soon'),
                 ('BldgSquareFeet', str, 'comming soon'),
                 ('NewParcelRoll', str, 'comming soon'),
                 ('InspectionDate', str, 'comming soon'),
                 ('Closed', str, 'comming soon')]

for arg in property_args:
    property_parser.add_argument(arg[0],type=arg[1],help=arg[2])
