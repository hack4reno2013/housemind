from flask.ext.restful import reqparse
sales_parser = reqparse.RequestParser()
sales_args = [('ParcelNumber',int,''),
    ('Sequence', str,''), 
    ('DocumentNumber', str,''),
    ('SaleUseCode', str,''),
    ('SaleVerificationCode', str,''),
    ('SaleDate', str,''), #should really be data
    ('SaleAmount', int,'')
]


for arg in sales_args:
    sales_parser.add_argument(arg[0],type=arg[1],help=arg[2])
