# -*- coding: utf-8 -*-
from schema import metadata
import settings


def drop_and_create_db(conn, db_name):
    """
    Drop the database if it exists, then create.
    """
    # Oh good lord: http://stackoverflow.com/q/5402805
    conn.connection.connection.set_isolation_level(0)
    conn.execute("DROP DATABASE IF EXISTS {db}".format(db=db_name))
    conn.execute("CREATE DATABASE {db}".format(db=db_name))
    conn.connection.connection.set_isolation_level(1) # TODO ?


def create_schema(conn):
    metadata.create_all(conn)


if __name__ == "__main__":

    # Create the engine
    from sqlalchemy import create_engine

    engine = create_engine(settings.CONN_STRING)

    # TODO confirm the drop if it already exists
    with engine.begin() as conn:
        drop_and_create_db(conn, settings.DB_NAME)

    # TODO how to switch into database without re-connecting?
    # /connect DB_NAME
    engine = create_engine(settings.DB_STRING)

    # TODO make all load scripts optional? Check for existing values first?
    with engine.begin() as conn:
        create_schema(conn)