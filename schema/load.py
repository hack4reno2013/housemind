# -*- coding: utf-8 -*-
import csv
import datetime
import sys
import os

import settings
from schema import properties


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
        'LandAppraised': line[19],
        'LandAssessed': line[20],
        'ImprovmentAppraised': line[21],
        'ImprovmentAssessed': line[22],
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


def load_properties(conn, csv_file):
    """
    Load the Properties.csv
    """
    # TODO Should be idempotent
    # Take the items in 10,000 item chunks
    # These are transactions, not connections!
    size = 10000
    with open(csv_file, "r") as f:
        lines = [l for l in csv.reader(f)]
        for i, c in enumerate(chunk(lines, size)):
            with engine.begin() as conn:
                print "Loading chunk {}, <= {}".format(i, size * (i + 1))
                conn.execute(properties.insert([clean_property(p) for p in c]))
            

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
        ("Property.csv", load_properties),
    ]

    # Check for all files before loading
    error = False
    for filename, method in files:
        csv_file = os.path.join(directory, filename)
        if not os.path.isfile(csv_file):
            print "There is no file name named", filename
            error = True

    if error:
        sys.exit(1)

    # Connect to the database
    from sqlalchemy import create_engine
    engine = create_engine(settings.DB_STRING)

    for filename, method in files:
        csv_file = os.path.join(directory, filename)
        method(engine, csv_file)
