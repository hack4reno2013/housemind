Housemind
=========

Let's mine the Washoe County assessor data!

http://www.washoecounty.us/assessor

You can query the property database here: http://www.washoecounty.us/assessor/cama/search.php

The data can also be download from: http://www.washoecounty.us/assessor/dl.htm

With the main generic data file ats: ftp://GenericFiles:endjob@wcftp.washoecounty.us/GNRC/generic.zip


To generate the CSV files from the assessor data, run the command `convert_to_csv.py` in the `python/` directory. No dependencies are needed.

    python convert_to_csv.py Property.txt

JSON files can be generated using `convert_to_json.py`. It takes an optional limit argument to output a specific number of items. No dependencies are needed.

    python convert_to_json.py Property.txt

    python convert_to_json.py Property.txt 20


To run the build script, there must be a PostGres installation and the following python dependencies must be installed:

* SQLAlchemy==0.8.2
* psycopg2==2.5.1

