import os
import sys
import json


splices = {
    "Property": [
        (1, 10),
        (11, 40),
        (41, 65),
        (66, 69),
        (70, 79),
        (80, 89),
        (90, 124),
        (125, 164),
        (165, 204),
        (205, 229),
        (230, 239),
        (240, 255),
        (256, 259),
        (260, 269),
        (270, 279),
        (280, 289),
        (290, 299),
        (300, 309),
        (310, 339),
        (340, 348),
        (349, 357),
        (358, 366),
        (367, 375),
        (376, 379),
        (380, 383),
        (384, 387),
        (388, 391),
        (392, 395),
        (396, 403),
        (404, 407),
        (408, 417),
        (418, 437),
        (438, 447),
        (448, 448),
    ],
    "Areas": [
        (1, 10),
        (11, 12),
        (13, 14),
        (15, 18),
        (19, 21),
        (22, 25),
        (26, 28),
        (29, 32),
    ],
    "Building": [
        (1, 10),
        (11, 12),
        (13, 37),
        (38, 41),
        (42, 45),
        (46, 49),
        (50, 53),
        (54, 57),
        (58, 61),
        (62, 65),
        (66, 68),
        (69, 72),
        (73, 75),
        (76, 79),
        (80, 83),
        (84, 86),
        (87, 90),
        (91, 93),
        (94, 97),
        (98, 100),
        (101, 105),
        (106, 110),
        (111, 115),
        (116, 119),
        (120, 121),
    ],
    "Drawn": [
        (1, 10),
        (11, 12),
        (13, 14),
        (15, 18),
        (19, 27),
    ],
    "Misc": [
        (1, 10),
        (11, 12),
        (13, 14),
        (15, 23),
        (24, 27),
        (28, 47),
        (48, 59),
    ],
    "Sales": [
        (1, 10),
        (11, 12),
        (13, 32),
        (33, 36),
        (37, 40),
        (41, 50),
        (51, 59),
    ],
    "Zone": [
        (1, 10),
        (11, 12),
        (13, 32),
        (33, 36),
        (37, 39),
    ],
}

fields = {
    "Property": [
        "ParcelNumber",
        "LastName",
        "FirstName",
        "EtAls",
        "SitusNumber",
        "SitusDirection",
        "SitusStreet",
        "MailingAddress1",
        "MailingAddress2",
        "MailingCity",
        "MailingState",
        "MailingZipCode",
        "TaxDistrict",
        "Township",
        "Section",
        "Lot",
        "Block",
        "Range",
        "Subdivision",
        "LandAppraised",
        "LandAssessed",
        "ImprovmentAppraised",
        "ImprovmentAssessed",
        "ReappraisalCycle",
        "LandUseCode",
        "Water",
        "Sewer",
        "StreetType",
        "LandArea",
        "LandUnittype",
        "BldgSquareFeet",
        "NewParcelRoll",
        "InspectionDate",
        "Closed",
    ],
    "Areas": [
        "ParcelNumber",
        "CardNumber",
        "Sequence",
        "Area",
        "PercentUsable",
        "AlternateType",
        "AlternatePercentage",
        "Quality",
    ],
    "Building": [
        "ParcelNumber",
        "CardNumber",
        "PropertyName",
        "Buildingtype",
        "QualityClass",
        "OrigConstructionYear",
        "AverConstruction Year",
        "NoofUnits",
        "Stories",
        "ExteriorWallsType1",
        "ExteriorPercent1",
        "ExteriorWallsType2",
        "ExteriorPercent2",
        "AvgStoryHeight",
        "Roofing",
        "HeatPercent",
        "HeatCool1",
        "HeatCoolPercent1",
        "HeatCool2",
        "HeatCoolPercent2",
        "Baths",
        "PlumbFixtures",
        "Bedrooms",
        "Shape",
        "BasementGarage", # Was BasementGrage
    ],
    "Drawn": [
        "ParcelNumber",
        "CardNumber",
        "Sequence",
        "SubAreaType",
        "SubAreaSF",
    ],
    "Misc": [
        "ParcelNumber",
        "CardNumber",
        "Sequence",
        "AdditiveCost",
        "Additive",
        "AdditiveArea",
        "Description",
    ],
    "Sales": [
        "ParcelNumber",
        "Sequence",
        "DocumentNumber",
        "SaleUseCode",
        "SaleVerificationCode",
        "SaleDate",
        "SaleAmount",
    ],
    "Zone": [
        "ParcelNumber",
        "CardNumber",
        "TempZoning",
        "Zoning",
        "ZoningPercent",
    ],

}

def convert_to_csv(filepath, name, splits, fields, limit=None):
    """
    Using the splits, break the filename into a csv.
    """
    zfs = zip(splits, fields)

    cols = []
    with open(filepath, "r") as f:
        if limit:
            for i in range(0, limit):
                l = f.readline()
                cols.append({field: l[s[0] - 1:s[1]].strip() for s, field in zfs})
        else:
            cols = [{field: l[s[0] - 1:s[1]].strip() for s, field in zfs} for l in f.readlines()]


    new_filename = "{name}.json".format(name=name)
    with open(new_filename, "w") as w:
        json.dump(cols, w)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please enter a filename to convert"
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print "Could not find file:", filepath
        sys.exit(1)

    path, filename = os.path.split(filepath)

    name, extension = os.path.splitext(filename)
    if name not in splices:
        print "Unrecognized filename:", name
        sys.exit(1)

    limit = int(sys.argv[2]) if len(sys.argv) == 3 else None
    convert_to_csv(filepath, name, splices[name], fields[name], limit=limit)
