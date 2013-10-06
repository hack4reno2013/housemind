# -*- coding: utf-8 -*-
from collections import defaultdict
import csv
import sys
import os

from sqlalchemy import select, update
from sqlalchemy.sql import and_

from schema import properties, buildings
import settings


def match_latlong(engine, filepath):
    """
    """
    matcher = defaultdict(list)

    with engine.begin() as conn:
        # TODO Use a like
        s = select([properties.c.SitusStreet, properties.c.SitusNumber, properties.c.ParcelNumber])

        results = conn.execute(s).fetchall()

        for street, number, parcel in results:
            matcher[(street, number)].append(parcel)

    # TODO Only match if there is a single address?
    # singles = {k: v[0] for k, v in matcher if len(v) == 1}
    # print "Single addresses are {0} of {1} items".format(len(singles), len(matcher))
    print "{} Addresses".format(len(matcher))

    attempts = 0
    matched = 0

    have_lat_long = defaultdict(list)

    with open(filepath) as f:
        csvr = csv.reader(f)
        header = csvr.next()

        for i, line in enumerate(csvr):
            # Only attempt a match if there is a lat / long
            lat = float(line[-2])
            lon = float(line[-1])

            if not (lat and lon):
                skipped += 1
                continue

            num = line[1].strip()
            num_suffix = line[2].strip()
            street_dir = line[3].strip()
            street = line[4].strip()
            street_type = line[5].strip()

            if num_suffix:
                number = "{}".format(int(float(num))) + " " + num_suffix
            else:
                number = "{}".format(int(float(num)))

            full_street = "{} {}".format(street, street_type)

            key = (full_street, number)

            # Attempt to match the address
            attempts += 1

            if key in matcher:
                matched += 1
                # Update the parcels with the lat long
                # TODO This is still broken, addresses are being overwritten?
                have_lat_long[key] = (matcher[key], (lat, lon))

    print "{} of {} Matched".format(matched, attempts)

    parcels = matcher[key]
    with engine.begin() as conn:

        for key, values in have_lat_long.items():
            parcel, ll = values
            lat, lon = ll
            u = update(properties).where(properties.c.ParcelNumber.in_(parcels)).values(Latitude=lat, Longitude=lon)
            result = conn.execute(u)
            print lat, lon, result.__dict__["rowcount"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Please enter the address file"
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print "Could not find file:", filepath
        sys.exit(1)

    # Connect to the database
    from sqlalchemy import create_engine
    engine = create_engine(settings.DB_STRING)

    match_latlong(engine, filepath)