# -*- coding: utf-8 -*-
import csv
import datetime
import sys
import os

import settings
from schema import properties, areas, buildings, sales, zones


conversions = {
    'sf': 1,
    'ac': 43560,
}

def convert_to_sf(value, unit):
    """
    Convert the given value and unit to square feet.
    """
    if not (value and unit):
        return None
    unit = unit.lower()
    if unit not in conversions:
        return None
    try:
        float_value = float(value)
    except ValueError:
        return None
    return int(float_value * conversions[unit])


def parse_assessor_date(value):
    """
    Convert the given assessor date string to a python datetime.date object.
    """
    if not value:
        return None
    try:
        dt = datetime.datetime.strptime(value, "%m/%d/%Y")
        if dt:
            return dt.date()
    except TypeError:
        pass
    return None


def parse_int(value):
    """
    Parse an int, that might look like a float.
    """
    if not value:
        return None
    try:
        return int(float(value))
    except ValueError:
        pass
    return none


def parse_float(value):
    """
    Parse a float.
    """
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        pass
    return None


def parse_bool(value):
    """
    Parse a boolean represented as 0 or 1.
    """
    if not value:
        return None
    try:
        return bool(int(value))
    except ValueError:
        pass
    return None



def clean_property(line):
    """
    Convert a property to load into the database.
    """
    # TODO logging
    return {
        'ParcelNumber': line[0],
        'LastName': line[1],
        'FirstName': line[2],
        'EtAls': line[3],
        'SitusNumber': line[4],
        'SitusDirection': line[5],
        'SitusStreet': line[6],
        'MailingAddress1': line[7],
        'MailingAddress2': line[8],
        'MailingCity': line[9],
        'MailingState': line[10],
        'MailingZipCode': line[11],
        'TaxDistrict': line[12],
        'Township': line[13],
        'Section': line[14],
        'Lot': line[15],
        'Block': line[16],
        'Range': line[17],
        'Subdivision': line[18],
        'LandAppraised': parse_int(line[19]),
        'LandAssessed': parse_int(line[20]),
        'ImprovmentAppraised': parse_int(line[21]),
        'ImprovmentAssessed': parse_int(line[22]),
        'ReappraisalCycle': line[23],
        'LandUseCode': line[24],
        'Water': line[25],
        'Sewer': line[26],
        'StreetType': line[27],
        # Land square feet is determined by LandArea and LandUnittype
        'LandSquareFeet': convert_to_sf(line[28], line[29]),
        'BldgSquareFeet': parse_int(line[30]),
        'NewParcelRoll': line[31],
        'InspectionDate': parse_assessor_date(line[32]),
        'Closed': parse_bool(line[33]),
    }


def clean_area(item):
    """
    Clean an area object
    """
    # An id will be set automatically
    return {
        'ParcelNumber': item[0],
        'CardNumber': item[1],
        'Sequence': item[2],
        'Area': item[3],
        'PercentUsable': parse_float(item[4]),
        'AlternateType': item[5],
        'AlternatePercentage': parse_float(item[6]),
        'Quality': item[7],
    }


def clean_building(item):
    """
    Clean a building object
    """
    # An id will be set automatically
    return {
        'ParcelNumber': item[0],
        'CardNumber': item[1],
        'PropertyName': item[2],
        'Buildingtype': item[3],
        'QualityClass': item[5],
        'OrigConstructionYear': parse_int(item[6]),
        'AverConstructionYear': parse_int(item[7]),
        'NoofUnits': parse_int(item[7]),
        'Stories': item[8],
        'ExteriorWallsType1': item[9],
        'ExteriorPercent1': parse_float(item[10]),
        'ExteriorWallsType2': item[11],
        'ExteriorPercent2': parse_float(item[12]),
        'AvgStoryHeight': parse_float(item[13]),
        'Roofing': item[14],
        'HeatPercent': parse_float(item[15]),
        'HeatCool1': item[16],
        'HeatCoolPercent1': parse_float(item[17]),
        'HeatCool2': item[18],
        'HeatCoolPercent2': parse_float(item[19]),
        'Baths': parse_float(item[20]),
        'PlumbFixtures': parse_int(item[21]),
        'Bedrooms': parse_int(item[22]),
        'Shape': item[23],
        'BasementGarage': parse_int(item[24]),
    }


def clean_sale(item):
    """
    Clean a sale object
    """
    # An id will be set automatically
    return {
        'ParcelNumber': item[0],
        'Sequence': item[1],
        'DocumentNumber': item[2],
        'SaleUseCode': item[3],
        'SaleVerificationCode': item[4],
        'SaleDate': parse_assessor_date(item[5]),
        'SaleAmount': parse_int(item[6]),
    }


def clean_zone(item):
    """
    Clean a zone item
    """
    return {
        'ParcelNumber': item[0],
        'CardNumber': item[1],
        'TempZoning': item[2],
        'Zoning': item[3],
        'ZoningPercent': parse_float(item[4]),
    }
    

def load(engine, csv_file, method, table):
    """
    Load the csv file after cleaning the results.
    """
    size = 10000
    with open(csv_file, "r") as f:
        lines = [l for l in csv.reader(f)]
        for i, c in enumerate(chunk(lines, size)):
            with engine.begin() as conn:
                print "Loading chunk {}, <= {}".format(i, size * (i + 1))
                conn.execute(table.insert([method(p) for p in c]))


def chunk(iterator, n):
    """
    Break the iterator into n sized chunks
    """
    for i in xrange(0, len(iterator), n):
        yield iterator[i:i + n]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Please specify the directory with the csv files"
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print "Given path is not a directory"
        sys.exit(1)

    files = [
        ("Property.csv", clean_property, properties),
        ("Areas.csv", clean_area, areas),
        ("Building.csv", clean_building, buildings),
        ("Sales.csv", clean_sale, sales),
        ("Zone.csv", clean_zone, zones),
    ]

    # Check for all files before loading
    error = False
    for filename, method, table in files:
        csv_file = os.path.join(directory, filename)
        if not os.path.isfile(csv_file):
            print "There is no file named", filename
            error = True

    if error:
        sys.exit(1)

    # Connect to the database
    from sqlalchemy import create_engine
    engine = create_engine(settings.DB_STRING)

    for filename, method, table in files:
        print "Loading file:", filename
        csv_file = os.path.join(directory, filename)
        load(engine, csv_file, method, table)
