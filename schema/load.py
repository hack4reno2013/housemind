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
    """
    if not value and unit:
        return None
    if unit not in conversions:
        return None
    try:
        float_value = float(value)
    except ValueError:
        return None
    return int(float_value * conversions[unit])


def clean_property(line):
    """
    Convert a property to load into the database.
    """
    # TODO logging
    prop = {
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
        'NewParcelRoll': line[31],
    }

    # Land square feet is determined by LandArea and LandUnittype
    area = line[28]
    unit = line[29].lower()

    prop['LandSquareFeet'] = convert_to_sf(area, unit)

    bldg = line[30]
    if bldg:
        try:
            prop['BldgSquareFeet'] = int(float(bldg))
        except ValueError:
            print "Count not convert the value '{}' to an integer square feet for '{}'".format(line[30], line[0]) 

    inspect = line[32]
    if inspect:
        try:
            prop['InspectionDate'] = datetime.datetime.strptime(inspect, "%m/%d/%Y").date()
        except TypeError:
            print "Count not convert the value '{}' to a date for '{}'".format(line[0], inspect)         

    try:
        prop['Closed'] = bool(int(line[33]))
    except ValueError:
        print "Count not convert the value '{}' to an boolean for '{}'".format(line[0], line[33])

    return prop


def load_properties(conn, csv_file):
    """
    Load the Properties.csv
    """
    # TODO Should be idempotent

    # TODO Probably doesn't need to chunk anymore
    chunk = 1000
    with open(csv_file, "r") as f:
        csvr = csv.reader(f)
        count = 0
        clean = []
        for line in csvr:
            clean.append(clean_property(line))
            count += 1
            if count > chunk:
                print "Loading chunk"
                with engine.begin() as conn:
                    conn.execute(properties.insert(clean))
                count = 0
                clean = []

    if clean:
        with engine.begin() as conn:
            conn.execute(properties.insert(clean))


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
