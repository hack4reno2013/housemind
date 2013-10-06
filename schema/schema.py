# -*- coding: utf-8 -*-
from sqlalchemy import MetaData, Table, Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import Integer, Date, String, Float, Integer, Boolean, BigInteger

metadata = MetaData()

properties = Table('properties', metadata,
    Column('ParcelNumber', String, primary_key=True),
    Column('LastName', String), # Corps only have last name
    Column('FirstName', String),
    Column('EtAls', String), # FK to TableOwnerType?
    Column('SitusNumber', String),
    Column('SitusDirection', String),
    Column('SitusStreet', String),
    Column('MailingAddress1', String),
    Column('MailingAddress2', String),
    Column('MailingCity', String),
    Column('MailingState', String),
    Column('MailingZipCode', String),
    Column('TaxDistrict', String),
    Column('Township', String),
    Column('Section', String),
    Column('Lot', String),
    Column('Block', String),
    Column('Range', String),
    Column('Subdivision', String),
    Column('LandAppraised', String), # Is this a value?
    Column('LandAssessed', String), # Is this a value?
    Column('ImprovmentAppraised', String), # Is this a value?
    Column('ImprovmentAssessed', String), # Is this a value?
    Column('ReappraisalCycle', String),
    Column('LandUseCode', String),
    Column('Water', String),
    Column('Sewer', String),
    Column('StreetType', String),
    Column('LandSquareFeet', BigInteger), # Replaces LandArea and LandUnittype
    Column('BldgSquareFeet', BigInteger),
    Column('NewParcelRoll', String),
    Column('InspectionDate', Date),
    Column('Closed', Boolean),
)

areas = Table('areas', metadata,
    Column('id', Integer, primary_key=True),
    Column('ParcelNumber', ForeignKey('properties.ParcelNumber')),
    Column('CardNumber', String), # Integer sequence?
    Column('Sequence', String), # Integer sequence?
    Column('Area', String),
    Column('PercentUsable', Float),
    Column('AlternateType', String),
    Column('AlternatePercentage', Float),
    Column('Quality', String),
    UniqueConstraint('ParcelNumber', 'CardNumber', 'Sequence', 'Area'),
)

buildings = Table('buildings', metadata,
    Column('id', Integer, primary_key=True),
    Column('ParcelNumber', ForeignKey('properties.ParcelNumber')),
    Column('CardNumber', String), # Integer Sequence?
    Column('PropertyName', String),
    Column('Buildingtype', String),
    Column('QualityClass', String),
    Column('OrigConstructionYear', Integer),
    Column('AverConstructionYear', Integer), # Was "AverConstruction Year"
    Column('NoofUnits', Integer),
    Column('Stories', String),
    Column('ExteriorWallsType1', String),
    Column('ExteriorPercent1', Float),
    Column('ExteriorWallsType2', String),
    Column('ExteriorPercent2', Float),
    Column('AvgStoryHeight', Float),
    Column('Roofing', String),
    Column('HeatPercent', Float),
    Column('HeatCool1', String),
    Column('HeatCoolPercent1', Float),
    Column('HeatCool2', String),
    Column('HeatCoolPercent2', Float),
    Column('Baths', Float),
    Column('PlumbFixtures', Integer),
    Column('Bedrooms', Integer),
    Column('Shape', String),
    Column('BasementGarage', Integer), # Was "BasementGrage"
    UniqueConstraint('ParcelNumber', 'CardNumber'),
)

sales = Table('sales', metadata,
    Column('id', Integer, primary_key=True),
    Column('ParcelNumber', ForeignKey('properties.ParcelNumber')),
    Column('Sequence', String), # Integer sequence?
    Column('DocumentNumber', String),
    Column('SaleUseCode', String),
    Column('SaleVerificationCode', String),
    Column('SaleDate', Date),
    Column('SaleAmount', Integer),
    UniqueConstraint('ParcelNumber', 'Sequence'),
)

zones = Table('zones', metadata,
    Column('id', Integer, primary_key=True),
    Column('ParcelNumber', ForeignKey('properties.ParcelNumber')),
    Column('CardNumber', String),
    Column('TempZoning', String),
    Column('Zoning', String),
    Column('ZoningPercent', Float),
    UniqueConstraint('ParcelNumber', 'CardNumber', 'TempZoning', 'Zoning'),
    # Or (ParcelNumber, CardNumber, TempZoning / Zoning)?
)