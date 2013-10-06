# -*- coding: utf-8 -*-
import csv
import sys
import os

from sqlalchemy import select, update

from schema import properties, buildings
import settings


def flatten_districts(engine, filename):
    """
    Flatten the "TaxDistrict" column of properties.
    """
    districts = {}
    with open(filename) as f:
        districts = {district: city for district, city in csv.reader(f)}

    # Query the database for each key and perform an update to replace the
    # district column
    for pk, name in districts.items():
        # Example select
        # s = select([properties.c.ParcelNumber]).where(properties.c.TaxDistrict == pk)

        with engine.begin() as conn:
            u = update(properties).where(properties.c.TaxDistrict == pk).values(TaxDistrict=name)
            result = conn.execute(u)
            # TODO Number of results changed?
            # print result


def flatten_roofing(engine, filename):
    """
    Flatten the "Roofing" column of buildings.
    """
    items = {}
    with open(filename) as f:
        items = {pk: name for pk, short, name in csv.reader(f)}

    for pk, name in items.items():
        with engine.begin() as conn:
            u = update(buildings).where(buildings.c.Roofing == pk).values(Roofing=name)
            result = conn.execute(u)
            
            # TODO Number of results changed?
            print pk, name, result.__dict__["rowcount"]


def flatten_walls(engine, filename):
    """
    Flatten the "ExteriorWallsType1" and ExteriorWallsType2" column of
    buildings.
    """
    items = {}
    with open(filename) as f:
        items = {pk: name for pk, short, name in csv.reader(f)}

    for pk, name in items.items():
        with engine.begin() as conn:
            u = update(buildings).where(buildings.c.ExteriorWallsType1 == pk).values(ExteriorWallsType1=name)
            result = conn.execute(u)
            
            # TODO Number of results changed?
            print pk, name, result.__dict__["rowcount"]

            u = update(buildings).where(buildings.c.ExteriorWallsType2 == pk).values(ExteriorWallsType2=name)
            result = conn.execute(u)
            print pk, name, result.__dict__["rowcount"]


def flatten_height(engine, filename):
    items = {}
    with open(filename) as f:
        items = {pk: name for pk, name in csv.reader(f)}

    for pk, name in items.items():
        with engine.begin() as conn:
            u = update(buildings).where(buildings.c.Stories == pk).values(Stories=name)
            result = conn.execute(u)
            
            # TODO Number of results changed?
            print pk, name, result.__dict__["rowcount"]


def flatten_heat(engine, filename):
    items = {}
    with open(filename) as f:
        items = {pk: name for pk, abbrev, name in csv.reader(f)}

    for pk, name in items.items():
        with engine.begin() as conn:
            u = update(buildings).where(buildings.c.HeatCool1 == pk).values(HeatCool1=name)
            result = conn.execute(u)
            
            # TODO Number of results changed?
            print pk, name, result.__dict__["rowcount"]

            u = update(buildings).where(buildings.c.HeatCool2 == pk).values(HeatCool2=name)
            result = conn.execute(u)
            
            # TODO Number of results changed?
            print pk, name, result.__dict__["rowcount"]


def flatten_street(engine, filename):
    items = {}
    with open(filename) as f:
        items = {pk: name for pk, name, comment in csv.reader(f)}

    for pk, name in items.items():
        with engine.begin() as conn:
            # TODO Why the strip?
            pk = pk.strip()
            # s = select([properties.c.StreetType]).where(properties.c.StreetType == pk)
            # print len(conn.execute(s).fetchall())

            u = update(properties).where(properties.c.StreetType == pk).values(StreetType=name)
            result = conn.execute(u)
            
            # TODO Number of results changed?
            print pk, name, result.__dict__["rowcount"]


def flatten_type(engine, filename):
    items = {}
    with open(filename) as f:
        items = {pk: name for pk, abbrev, name in csv.reader(f)}

    for pk, name in items.items():
        with engine.begin() as conn:
            # TODO Why the strip?
            pk = pk.strip()

            # s = select([properties.c.StreetType]).where(properties.c.StreetType == pk)
            # print len(conn.execute(s).fetchall())

            u = update(buildings).where(buildings.c.Buildingtype == pk).values(Buildingtype=name)
            result = conn.execute(u)
            
            # TODO Number of results changed?
            print pk, name, result.__dict__["rowcount"]


files = [
    ("TableDistrictType.txt", flatten_districts),
    ("TableRoofMaterial.txt", flatten_roofing),
    ("TableExteriorWall.txt", flatten_walls),
    ("TableStoryHeight.txt", flatten_height),
    ("TableHeatType.txt", flatten_heat),
    ("TableStreetCond.txt", flatten_street),
    ("TableBuildingType.txt", flatten_type),
]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Please specify the directory with the support table files"
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print "Given path is not a directory"
        sys.exit(1)

    error = False
    for filename, method in files:
        csv_file = os.path.join(directory, filename)
        if not os.path.isfile(csv_file):
            print "There is no file named", filename
            error = True

    if error:
        sys.exit(1)

    # Connect to the database
    from sqlalchemy import create_engine
    engine = create_engine(settings.DB_STRING)

    for filename, method in files:
        print "Loading file:", filename
        csv_file = os.path.join(directory, filename)
        method(engine, csv_file)
