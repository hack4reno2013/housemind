Queries
=======

Some example queries you can run against the database.

    SELECT "SitusNumber" as num, "SitusDirection" as dir, "SitusStreet" as street FROM properties;


Count the number of properties per MailingCity

    SELECT count("MailingCity") as num, "MailingCity" as city FROM properties GROUP BY "MailingCity" ORDER BY num DESC;

    SELECT avg("LandSquareFeet") as size, "MailingCity" as city FROM properties GROUP BY "MailingCity" ORDER BY size DESC;


Sales over $1 million by date:

    SELECT "SitusNumber" as num, "SitusStreet" as street, "MailingCity" as city, "SaleDate" as date, "SaleAmount" FROM sales JOIN properties ON sales."ParcelNumber" = properties."ParcelNumber" WHERE "SaleAmount" > 1000000 ORDER BY "SaleDate" DESC LIMIT 20;


Oldest buildings:

    SELECT "ParcelNumber", "PropertyName", "OrigConstructionYear" FROM buildings WHERE "OrigConstructionYear" <> 0 ORDER BY "OrigConstructionYear" LIMIT 20;

    SELECT properties."SitusNumber" as "#", properties."SitusStreet" as street, properties."MailingCity", "PropertyName", "OrigConstructionYear" as year FROM buildings JOIN properties ON buildings."ParcelNumber" = properties."ParcelNumber" WHERE "OrigConstructionYear" <> 0 AND "MailingState" = 'NV' ORDER BY "OrigConstructionYear" LIMIT 20;