Housemind
=========


Let's mine the [Washoe County assessor](http://www.washoecounty.us/assessor) data!

* [You can query the property database here](http://www.washoecounty.us/assessor/cama/search.php)
* [The data can also be download from href](http://www.washoecounty.us/assessor/dl.htm)
* [With the main generic data file here](ftp://GenericFiles:endjob@wcftp.washoecounty.us/GNRC/generic.zip)


### Build

Copy the `example_settings.py` to `settings.py` and adjust the database connection strings for whatever database install you want to use.

To generate the CSV files from the assessor data, run the command `convert_to_csv.py` in the `python/` directory. No dependencies are needed.

    python convert_to_csv.py Property.txt

Sample JSON files can be also generated using `convert_to_json.py`. It takes an optional limit argument to output a specific number of items. No dependencies are needed.

    python convert_to_json.py Property.txt

    python convert_to_json.py Property.txt 20

To run the build script, there must be a PostGres installation and the following python dependencies must be installed:

* SQLAlchemy==0.8.2

To build, run these scripts in the `schema` dir (or use the build file!):

    python build.py
    python load.py <path to .csv data>
    python flatten.py <path to support data>
    python latlong.py <path to address file>
