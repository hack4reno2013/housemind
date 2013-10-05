# -*- coding: utf-8 -*-
from sqlalchemy import MetaData, Table, Column, ForeignKey, UniqueConstraint, PrimaryKey
from sqlalchemy.types import Integer, Date, String, Float, Integer, Boolean

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
    Column('LandSquareFeet', Integer), # Replaces LandArea and LandUnittype
    Column('BldgSquareFeet', Integer),
    Column('NewParcelRoll', String),
    Column('InspectionDate', Date),
    Column('Closed', Boolean),
)

areas = Table('areas', metadata,
    # Composite Primary Key of (ParcelNumber, CardNumber, Sequence, Area)
    Column('ParcelNumber', ForeignKey('properties.ParcelNumber'), primary_key=True),
    Column('CardNumber', String, primary_key=True),
    Column('Sequence', String, primary_key=True), # Integer sequence?
    Column('Area', String, primary_key=True),
    Column('PercentUsable', Float),
    Column('AlternateType', String),
    Column('AlternatePercentage', Float),
    Column('Quality', String),
)