import csv
import os
import sys


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

def convert_to_csv(filepath, name, splits):
    """
    Using the splits, break the filename into a csv.
    """
    cols = []
    with open(filepath, "r") as f:
        cols = [[l[s - 1:e].strip() for s, e in splits] for l in f.readlines()]

    new_filename = "{name}.csv".format(name=name)
    with open(new_filename, "w") as w:
        csvw = csv.writer(w)
        csvw.writerows(cols)


if __name__ == "__main__":
    if len(sys.argv) != 2:
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

    convert_to_csv(filepath, name, splices[name])
