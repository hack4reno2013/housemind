Queries
=======

Some example queries you can run against the database.

```sql
SELECT "SitusNumber" as num, "SitusDirection" as dir, "SitusStreet" as street FROM properties;
```


Count the number of properties per MailingCity

```sql
SELECT count("MailingCity") as num, "MailingCity" as city FROM properties GROUP BY "MailingCity" ORDER BY num DESC;
```

```sql
SELECT avg("LandSquareFeet") as size, "MailingCity" as city FROM properties GROUP BY "MailingCity" ORDER BY size DESC;
```

Sales over $1 million by date:

```sql
SELECT "SitusNumber" as num, "SitusStreet" as street, "MailingCity" as city, "SaleDate" as date, "SaleAmount" FROM sales JOIN properties ON sales."ParcelNumber" = properties."ParcelNumber" WHERE "SaleAmount" > 1000000 ORDER BY "SaleDate" DESC LIMIT 20;
```

Oldest buildings:

```sql
SELECT properties."SitusNumber" as "#", properties."SitusStreet" as street, properties."MailingCity", "PropertyName", "OrigConstructionYear" as year FROM buildings JOIN properties ON buildings."ParcelNumber" = properties."ParcelNumber" WHERE "OrigConstructionYear" <> 0 AND "MailingState" = 'NV' ORDER BY "OrigConstructionYear" LIMIT 20;
```

Most expensive sales:

```sql
SELECT DISTINCT "SitusNumber" as num, "SitusStreet" as street, "MailingCity" as city, "SaleDate" as date, "SaleAmount" FROM sales JOIN properties ON sales."ParcelNumber" = properties."ParcelNumber" WHERE "MailingState" = 'NV' ORDER BY "SaleAmount" DESC LIMIT 20;
```

Average number of baths by city:

```sql
SELECT properties."MailingCity", AVG("Baths") as baths FROM buildings JOIN properties ON buildings."ParcelNumber" = properties."ParcelNumber" WHERE "MailingState" = 'NV' GROUP BY properties."MailingCity" ORDER BY baths DESC;
```