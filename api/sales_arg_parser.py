from flask.ext.restful import reqparse
from extra_types import int_range
sales_parser = reqparse.RequestParser()
sales_args = [('ParcelNumber',str,''),
    ('Sequence', str,''), 
    ('DocumentNumber', str,''),
    ('SaleUseCode', str,''),
    ('SaleVerificationCode', str,''),
    ('SaleDate', str,''), #should really be data
    ('SaleAmount', int_range,'')
]


for arg in sales_args:
    sales_parser.add_argument(arg[0],type=arg[1],help=arg[2])
