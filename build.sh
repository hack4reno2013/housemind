#!/bin/bash
echo "fetching latest data file"
wget ftp://GenericFiles:endjob@wcftp.washoecounty.us/GNRC/generic.zip
echo "unzipping"
unzip generic.zip
echo "building csv files"
python ./python/convert_to_csv.py ./GENERIC/Data\ Files/Property.txt
python ./python/convert_to_csv.py ./GENERIC/Data\ Files/Areas.txt
python ./python/convert_to_csv.py ./GENERIC/Data\ Files/Zone.txt
python ./python/convert_to_csv.py ./GENERIC/Data\ Files/Building.txt
python ./python/convert_to_csv.py ./GENERIC/Data\ Files/Sales.txt
echo "building database"
python ./schema/build.py
echo "populating database"
python ./schema/load.py ./
echo "cleaning up"
rm *.csv
rm -rf ./GENERIC
rm generic.zip